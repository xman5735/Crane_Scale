import serial.tools.list_ports
import os

# Get user input for filename
filename = input("Enter a name for the text file: ")

# Get list of available com ports
com_ports = list(serial.tools.list_ports.comports())

# Print available com ports
print("Available COM Ports:")
for port, desc, hwid in com_ports:
    print(f"{port} - {desc}")

# Get user input for which com port to use
com_port = input("Enter the COM port to use (e.g. COM1): ")

# Open the serial port at 115200 baud rate
ser = serial.Serial(com_port, baudrate=115200)

# Get user's desktop folder path
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# Open file for writing
file_path = os.path.join(desktop_path, f"{filename}.txt")
with open(file_path, "w") as f:
    # Read data from serial and write to file
    while True:
        data = ser.readline().decode("utf-8")
        f.write(data)
