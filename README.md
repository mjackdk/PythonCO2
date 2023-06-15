# ambientco2
*Python module for CozIR Ambient CO2 sensors*

The CozIR Ambient family of sensors all provide CO2 measurements, at different ranges. Some are able to measure temperature and relative humidity as well. The sensors use serial UART and analog voltage output.

This library has been developed using a **CozIR Ambient 0-5000 ppm CO2 (only)** sensor.


# Development

Milestone | Features | Version | Status
-------- | -------- | -------- | --------
Beta | Basic reading | 0.x.x | :heavy_check_mark:
Launch | Modes, settings | 1.x.x |
Sensors | Range, CO2, relative humidity, temperature | 2.x.x |


# Library Documentation

Add the following line to use this library:
``` python
from ambientco2 import Sensor
```

Further documentation on [Read the Docs](https://ambientco2.readthedocs.io/en/latest/index.html)

## Member functions

Name | Parameters | Returns | Description
-------- | -------- | -------- | --------
Sensor() | str serial_device | void | Constructor
setup() | int mode, int fields | void | Sensor setup
read() | str value | int | Reads CO2 concentration in PPM


# Installation

## pip
``` bash
$ pip install ambientco2
```

# Usage
``` python
from ambientco2 import Sensor

serial_device = "/dev/ttyUSB0"    # Debian (Ubuntu, Raspberry Pi OS etc.)

sensor = Sensor(serial_device)

co2 = sensor.read()

print(type(co2))
print(co2)
```

See [get_co2.py](https://github.com/mjackdk/PythonCO2/blob/main/get_co2.py) for a basic example

# Sensor Documentation

* [Product page](https://www.co2meter.com/collections/0-1-co2/products/cozir-ambient-5000-ppm-co2-sensor)
* [Data sheet](https://cdn.shopify.com/s/files/1/0019/5952/files/Datasheet_COZIR_A_CO2Meter_4_15.pdf)
* [User's Manual](http://co2meters.com/Documentation/Manuals/Manual_GC_0024_0025_0026_Revised8.pdf)
* [Application Note](http://www.co2meters.com/Documentation/AppNotes/AN127-COZIR-sensor-raspberry-pi-uart.pdf)
  and [sample code](http://www.co2meters.com/Documentation/AppNotes/AN127-COZIR-sensor-raspberry-pi.zip)


