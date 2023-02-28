import serial
import matplotlib.pyplot as plt
from datetime import datetime,time

# initialize serial connection
ser = serial.Serial('COM6', 115200)

# skip first 50 lines of serial to bypass config
for i in range(50):
    ser.readline()

# make list to store data
times = []
data = []

# get first time to set start time
line = ser.readline().decode().strip()
date, time_str, data_value, _ = line.split(',')
time_value = datetime.strptime(time_str, '%H:%M:%S.%f').time()
# convert time into seconds
start_time = (time_value.hour * 3600) + (time_value.minute * 60) + time_value.second

# read data from serial port
while True:
    line = ser.readline().decode().strip()
    if line:
        # parse data from serial input
        date, time_str, data_value, _ = line.split(',')
        time_value = datetime.strptime(time_str, '%H:%M:%S.%f').time()

        # convert time into seconds and subtract start time
        time_seconds = (time_value.hour * 3600) + (time_value.minute * 60) + time_value.second
        zero_time = time_seconds - start_time

        # add data to lists
        times.append(zero_time)
        data.append(float(data_value))

        # plot data
        plt.plot(times, data)
        plt.xlabel('Time (s)')
        plt.ylabel('Weight (?)')
        plt.title('Scale Weight Graph')
        plt.draw()
        plt.pause(0.1)
        plt.show()
