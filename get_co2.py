from ambientco2 import Sensor

######## CozIR Ambient sensor to Raspberry Pi GPIO #########
#                                                          #
#                See <https://pinout.xyz/>                 #
#                                                          #
#  PIN 3 (3.3V) ->   3V3  (1) (2)  5V                      #
#                  GPIO2  (3) (4)  5V                      #
#                  GPIO3  (5) (6)  GND                     #
#                  GPIO4  (7) (8)  GPIO14  <- PIN 5 (RXD)  #
#  PIN 1 (GND) ->    GND  (9) (10) GPIO15  <- PIN 7 (TXD)  #
#                                                          #
############################################################

########## CozIR Ambient sensor to console cable ###########
#                                                          #
#        See <https://www.adafruit.com/product/954>        #
#                                                          #
#               PIN 7 (TXD)  ->  White lead                #
#               PIN 5 (RXD)  ->  Green lead                #
#               PIN 3 (3.3V) ->  Red lead                  #
#               PIN 1 (GND)  ->  Black lead                #
#                                                          #
############################################################

# Uncomment according to setup
serial_device = "/dev/ttyUSB0"    # Debian (Ubuntu, Raspberry Pi OS etc.)

sensor = Sensor(serial_device)

co2 = sensor.read()

print(type(co2))
print(co2)