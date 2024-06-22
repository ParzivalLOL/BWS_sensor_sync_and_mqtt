import paho.mqtt.subscribe as subscribe
import datetime

while True: 
    file = open("C:\\Users\\Admin\\Desktop\\programming\\BWS\\datasets\\emg_fingers_1.csv", "a")
    sensor1 = subscribe.simple("emg/data", hostname="192.168.109.119")
    sensor2 = subscribe.simple("emg2/data", hostname="192.168.109.119")
    print(sensor1.payload)
    print(sensor2.payload)
    temp = str(sensor1.payload.decode('utf-8')) + "," + str(sensor2.payload.decode('utf-8'))
    file.write(temp + '\n')
    file.flush()
    file.close()