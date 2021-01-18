from ambientco2 import Sensor

###### CozIR Ambient connection to Raspberry Pi GPIO #######
#                                                          #
#  PIN 3 (3.3V) ->   3V3  (1) (2)  5V                      #
#                  GPIO2  (3) (4)  5V                      #
#                  GPIO3  (5) (6)  GND                     #
#                  GPIO4  (7) (8)  GPIO14  <- PIN 5 (RXD)  #
#  PIN 1 (GND) ->    GND  (9) (10) GPIO15  <- PIN 7 (TXD)  #
#                                                          #
############################################################

# Uncomment according to setup
serial_device = "/dev/ttyUSB0"    # Linux

sensor = Sensor(serial_device)

print("----- init -----")
print("")

print("----- setup -----")
print("Mode: " + str(sensor.mode))
print("Fields: " + str(sensor.fields))
print("")

print("----- measuremnt -----")
co2 = sensor.get_measurement()

print(co2)