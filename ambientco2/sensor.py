import serial
import time

class Sensor:
    """Core class of ambientco2, defaults to polling CO2 measurements

    Parameters:
        serial_device (string): Path to serial device, e.g. '/dev/ttyUSB0'
    """

    # Allowed modes, output_fields and values
    __modes = {
        "CMD": 0,
        "STR": 1,
        "POL": 2
    }
    __output_fields = {
        "CO2": 4,
        "HUM": 64,
        "TMP": 4096,
        "ALL": 4165
    }
    __value = {
        "CO2": "Z",
        "HUM": "H",
        "TMP": "T"
    }

    # Default mode and fields 
    __default_mode = "POL"
    __default_fields = "CO2"

    def __init__(self, serial_device):
        """Creates serial connection to sensor, calls setup() with defaults

        Parameters:
            serial_device (string): Path to serial device, e.g. '/dev/ttyUSB0'

        Returns:
            void
        """

        self.__serial_device = serial_device

        self.__connected = False

        self.__mode = Sensor.__default_mode
        self.__fields = Sensor.__default_fields

        try:
            self.__connection = serial.Serial(
                port = serial_device,
                baudrate = 9600,              # Only supported baud rate
                bytesize = serial.EIGHTBITS,
                parity = serial.PARITY_NONE,
                stopbits = serial.STOPBITS_ONE
            )
            self.__connected = True
            self.__setup()

        except:
            print("Could not establish serial connection to sensor")

    def __setup(self):
        """Sets up sensor (operation) mode and (output) fields

        Use 'mode' and 'fields' properties to change default setup
        """

    @property
    def mode(self):
        """Operating mode property

        Possible values are: 'CMD', 'STR' and 'POL'

        Set with 'self.mode = MODE'

        Returns:
            mode (string): current mode
        """
        return self.__mode

    @mode.setter
    def mode(self, mode):
        if mode not in Sensor.__modes:
            raise ValueError("Mode value is not valid")
        if self.__mode != mode:
            self.__mode = mode
            self.__setup()

    @property
    def fields(self):
        """Output fields property

        Possible values are 'CO2', 'HUM', 'TMP' and 'ALL'

        Set with 'self.fields = FIELDS'

        Returns:
            fields (string): current fields
        """
        return self.__fields

    @fields.setter
    def fields(self, fields):
        if fields not in Sensor.__output_fields:
            raise ValueError("Fields value is not valid")
        if self.__fields != fields:
            self.__fields = fields
            self.__setup()

    @property
    def status(self):
        """Status property (read-only)

        Returns a string with connection status, current mode and fields

        Returns:
            status (string): status message
        """
        if self.__connected:
            status = f"Device: '{self.__serial_device}', " \
            f"mode: {self.__mode}, fields: {self.__fields}"
        else:
            status = f"Sensor NOT connected, check '{self.__serial_device}'"
        return status

    def read(self):
        """Reads buffer from serial connection and returns measurement(s)

        Uses 'self.fields' to determine which measurement(s) to return
        """
        pass


