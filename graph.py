#DOESNT WORK ONLY FOR REFERENCE
import pandas as pd
import matplotlib.pyplot as plt

def set_range(index):
    centre = (index.max() + index.min())/2
    limits = [centre - 2, centre + 2]
    return limits

file_path_error = "C:\\Users\\Admin\\Desktop\\programming\\BWS\\datasets\\correction_set.csv"
file_path = "C:\\Users\\Admin\\Desktop\\programming\\BWS\\datasets\\mpu.csv"
column_names = ["timeStamp", "acclx", "accly", "acclz", "gyrox", "gyroy", "gyroz"]
column_names_error = ["acclx", "accly", "acclz", "gyrox", "gyroy", "gyroz"]

df_error = pd.read_csv(file_path_error, names=column_names_error)
df_error = df_error.apply(pd.to_numeric, errors="coerce")
averages = df_error.mean()

df = pd.read_csv(file_path, names=column_names)
df-=averages

acclx = df["acclx"]
accly = df["accly"]
acclz = df["acclz"]
gyrox = df["gyrox"]
gyroy = df["gyroy"]
gyroz = df["gyroz"]
timeStamp = df["timeStamp"]

figure, axis = plt.subplots(2,3)

axis[0,0].plot(acclx)
axis[0,0].set_title("Accleration X")
axis[0,0].set_ylim([set_range(acclx)[0], set_range(acclx)[1]])

axis[0,1].plot(accly)
axis[0,1].set_title("Accleration Y")
axis[0,1].set_ylim(set_range(accly)[0], set_range(accly)[1])

axis[0,2].plot(acclz)
axis[0,2].set_title("Accleration Y")
axis[0,2].set_ylim(set_range(acclz)[0], set_range(acclz)[1])

axis[1,0].plot(gyrox)
axis[1,0].set_title("Gyro X")
axis[1,0].set_ylim(set_range(gyrox)[0], set_range(gyrox)[1])

axis[1,1].plot(gyroy)
axis[1,1].set_title("Gyro Y")
axis[1,1].set_ylim(set_range(gyroy)[0], set_range(gyroy)[1])

axis[1,2].plot(gyroz)
axis[1,2].set_title("Gyro Z")
axis[1,2].set_ylim(set_range(gyroz)[0], set_range(gyroz)[1])

plt.show()