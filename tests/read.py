import ambientco2
import serial

########## CozIR connection to Raspberry Pi GPIO ###########
#                                                          #
#  PIN 3 (3.3V) ->   3V3  (1) (2)  5V                      #
#                  GPIO2  (3) (4)  5V                      #
#                  GPIO3  (5) (6)  GND                     #
#                  GPIO4  (7) (8)  GPIO14  <- PIN 5 (RXD)  #
#  PIN 1 (GND) ->    GND  (9) (10) GPIO15  <- PIN 7 (TXD)  #
#                                                          #
############################################################

serial_device = "/dev/ttyS0"     # Raspberry Pi Zero/3/4

connection = serial.Serial(serial_device)

ambientco2.setup(connection)

co2 = ambientco2.read(connection)

print(co2)

