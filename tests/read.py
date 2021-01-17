import ambientco2
import serial


serial_device = "/dev/ttyS0"     # Raspberry Pi Zero/3/4

connection = serial.Serial(serial_device)

ambientco2.setup(connection)

co2 = ambientco2.read(connection)

print(co2)

