import serial

class Sensor:

    baud_rate = 9600
    modes = (0,1,2)
    output_fields = (4,64,4096,4164)

    def __init__(self, serial_device):
        self.__device = serial_device
        self.setup()

    def setup(self):
        self.mode = 2
        self.fields = 4

    def measure(self):
        pass
    
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

    def get_measurement(self):
        self.measure()
        return 456
