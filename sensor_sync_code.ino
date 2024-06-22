//import libraries
#include <Arduino.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h> 
#include <WiFi.h>
#include <PubSubClient.h>

//establishing variable
const char* ssid = "AarjavS20FE"; //WiFi name
const char* password = "11112019"; //WiFi password
const char* mqtt_server = "192.168.151.154"; //IP address of reiciever or subscriber
const int mqtt_port = 1883; // DO NOT CHANGE

// Define the analog input pin for the EMG sensor 
const int emgPin = 34; // ESP32

// Variables to store EMG Data
int emgValue = 0;

WiFiClient espClient; //Creating the object
PubSubClient client(espClient); //Another object
Adafruit_MPU6050 mpu; //Yet another object

void setup() {
  // Initialize Serial communication
  Serial.begin(115200);
  WiFi.begin(ssid,password); //begins comms
  
  //for debugging
  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print("Wifi connecting");
  }

  Serial.println("Wifi connected");
  client.setServer(mqtt_server, mqtt_port);
  
  if(!mpu.begin()) {
    Serial.println("EMG not found");
  }
  // Set the resolution for the analog read (0-4095 ESP32)
  analogReadResolution(12); // 3.3(V)/2^12 =4096=3.3 V levels so that there is more accuracy if there is a change in the muscle activity

  // Set ADC attenuation - reduction of the strength/intensity of a signal (0-3V for EMG sensors typically)
  // ADC can do safely till 1.1V - thats why need to reduce
  analogSetAttenuation(ADC_11db);

  //Defining the ranges, high ranges means less accuracy
  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
}

void reconnect() {
  while(!client.connected()) {
    Serial.println("Reconnecting ");
    if(client.connect("ESP32CLIENT ")) {
      Serial.println("Connected to MQTT broker ");
    } else {
      delay(500);
    }
  }
}

void loop() {
  // Read the analog value from the EMG sensor
  emgValue = analogRead(emgPin);
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  if(!client.connected()) {
    reconnect();
  }
  client.loop();
  int timestamp = millis();
  String payload = String(emgValue) +","+ String(a.acceleration.x) + "," + String(a.acceleration.y) + "," + String(a.acceleration.z);
  client.publish("test4/topic", (char*) payload.c_str());
  // Print the EMG value to the Serial Monitor 
  delay(100);
}
