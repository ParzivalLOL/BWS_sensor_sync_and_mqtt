# Step 1: Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

def set_range(index):
    range = df[index].max() - df[index].min()
    margin = 0.1 * range
    limits = [df[index].min() - margin, df[index].max() + margin]
    return limits

# Step 2: Define the file path and column names
file_path_error = "C:\\Users\\Admin\\Desktop\\programming\\BWS\\datasets\\correction_set.csv"
file_path = "C:\\Users\\Admin\\Desktop\\programming\\BWS\\datasets\\mpu.csv"
column_names_err = ["AcclX", "AcclY", "AcclZ", "GyroX", "GyroY", "GyroZ"]
column_names = ["TimeStamp","AcclX", "AcclY", "AcclZ", "GyroX", "GyroY", "GyroZ"]

# Step 3: Read the CSV file into a DataFrame with specified column names
df_error = pd.read_csv(file_path_error, names=column_names_err)

# Step 4: Convert columns to numeric type, coercing errors to NaN
df_error = df_error.apply(pd.to_numeric, errors='coerce')

# Step 5: Handle missing values (e.g., fill NaNs with the mean of each column)
averages = df_error.mean()

df = pd.read_csv(file_path, names=column_names)
df -= averages
max = df.max()
min = df.min()
# Step 6: Extract the columns
AcclX = df["AcclX"]
AcclY = df["AcclY"]
AcclZ = df["AcclZ"]
GyroX = df["GyroX"]
GyroY = df["GyroY"]
GyroZ = df["GyroZ"]
TimeStamp = df["TimeStamp"]

# Step 7: Calculate the averages of each column and center the data
averages = df.mean()
df = df - averages

# Step 8: Create subplots
figure, axis = plt.subplots(2, 3)

# Step 9: Plot the data with titles and axis limits

axis[0, 0].plot(TimeStamp, AcclX)
axis[0, 0].set_title("Acceleration in the X axis")
axis[0, 0].set_xlim([125760, 167077])
axis[0, 0].set_ylim(set_range("AcclX")[0], set_range("AcclX")[1])

axis[0, 1].plot(AcclY)
axis[0, 1].set_title("Acceleration in the Y axis")
axis[0, 1].set_xlim([0, 1500])
#axis[0, 1].set_ylim(set_range(1)[0], set_range(1)[1])

axis[0, 2].plot(AcclZ)
axis[0, 2].set_title("Acceleration in the Z axis")
axis[0, 2].set_xlim([0, 1500])
#axis[0, 2].set_ylim(set_range(2)[0], set_range(2)[1])

axis[1, 0].plot(GyroX)
axis[1, 0].set_title("Rotation in the X axis")
axis[1, 0].set_xlim([0, 1500])
#axis[1, 0].set_ylim(set_range(3)[0], set_range(3)[1])

axis[1, 1].plot(GyroY)
axis[1, 1].set_title("Rotation in the Y axis")
axis[1, 1].set_xlim([0, 1500])
#axis[1, 1].set_ylim(set_range(4)[0], set_range(4)[1])

axis[1, 2].plot(GyroZ)
axis[1, 2].set_title("Rotation in the Z axis")
axis[1, 2].set_xlim([0, 1500])
#axis[1, 2].set_ylim(set_range(5)[0], set_range(5)[1])

# Step 10: Display the plots
plt.show()
