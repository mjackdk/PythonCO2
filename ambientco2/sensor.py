import serial
import time

"""
sensor.py
=========
Core module of ambientco2

"""
class Sensor:
    """
    Main ambientco2 class: initiation, setup and measurements methods
    """
    modes = (0,1,2)
    output_fields = (4,64,4096,4164)
    values = ("Z","H","T")

    def __init__(self, serial_device):
        """
        Initiates sensor and calls setup(), returns nothing
        
        Parameters
        ----------
        serial_device
            A string pointing to the serial device to use with the sensor
        
        """
        try:
            self.__connection = serial.Serial(
                port = serial_device, 
                baudrate = 9600,
                bytesize = serial.EIGHTBITS,
                parity = serial.PARITY_NONE,
                stopbits = serial.STOPBITS_ONE
            )
            self.setup()
        except:
            print("Could not establish serial connection to sensor")

    def setup(self, mode = 2, fields = 4):
        """
        Called by __init__, and possibly later, returns nothing
        
        Parameters
        ----------
        mode
            Integer indicating sensor mode: 0 is command mode, 1 is streaming 
            mode and 2 is polling mode. Defaults to 2 (polling mode)
        
        fields
            Integer indicating output fields (CO2, temperature and humidity).
            4 is CO2 only, 64 is temperature only, 4096 is humidity only and
            4164 all three. Defaults to 4 (CO2 only)

        """
        self.mode = mode
        self.fields = fields
        self.__connection.write(bytes("K " + str(self.mode) + "\r\n", "utf-8"))
        self.__connection.write(bytes("M " + str(self.fields) + "\r\n", "utf-8"))
        time.sleep(0.1)
        self.__connection.flushInput()

    @property
    def mode(self):
        return self.__mode
    
    @mode.setter
    def mode(self, mode):
        if mode not in self.modes:
            raise ValueError("Mode is not valid")
        self.__mode = mode

    @property
    def fields(self):
        return self.__fields

    @fields.setter
    def fields(self, fields):
        if fields not in self.output_fields:
            raise ValueError("Fields is not valid")
        self.__fields = fields
   
    def read(self, value = "Z"):
        if value not in self.values:
            raise ValueError("Value is not valid")
        self.value = value

        self.__connection.write(bytes(str(self.value) + "\r\n", "utf-8"))
        self.raw_measurement = self.__connection.read(10)
        self.measurement = int(self.raw_measurement[2:8])
        return self.measurement

if __name__ == '__main__':
    print("See <https://github.com/mjackdk/PythonCO2> for instructions")
