Getting started
===============
The following 4 steps are needed to obtain a reading from the sensor.

Set up hardware
------------------
Use one of the following methods to make a serial connection to the sensor:

a) USB to serial cable
^^^^^^^^^^^^^^^^^^^^^^
See `USB to TTL Serial Cable <https://www.adafruit.com/product/954>`_ for a 
tested cable.

+--------------+---------------------+
| Sensor       | USB to serial cable |
+==============+=====================+
| Pin 1 (GND)  | black (ground)      |
+--------------+---------------------+
| Pin 3 (3.3V) | red (power)         |
+--------------+---------------------+
| Pin 5 (RXD)  | green (TX)          |
+--------------+---------------------+
| Pin 7 (TXD)  | white (RX)          |
+--------------+---------------------+

b) Raspberry Pi GPIO
^^^^^^^^^^^^^^^^^^^^
See `Raspberry Pi pinout <https://pinout.xyz/>`_ for an overview of the GPIO 
pins.

+--------------+------------------+
| Sensor       | GPIO pin         |
+==============+==================+
| Pin 1 (GND)  | Pin 9 (GND)      |
+--------------+------------------+
| Pin 3 (3.3V) | Pin 1 (3V3)      |
+--------------+------------------+
| Pin 5 (RXD)  | Pin 8 (GPIO 14)  |
+--------------+------------------+
| Pin 7 (TXD)  | Pin 10 (GPIO 15) |
+--------------+------------------+

Determine device
-------------------

Use the *ls* command in a terminal to find the device used for serial 
connection to the sensor.

With 'ls -1', the output is one line per file:

.. code-block:: bash

   $ ls -1 /dev/tty*
   ...
   /dev/ttyS9
   /dev/ttyUSB0

In this example from Ubuntu 20.10 on x86_64, the device for serial connection 
to the sensor is '/dev/ttyUSB0'.

If unsure which one is the device used for sensor connection, 
run the command with and without the sensor plugged in, and notice the 
difference.

Install module
-----------------
The module can be installed with *pip*:

.. code-block:: bash

   $ pip install ambientco2


Run example script
---------------------
To print a single CO2 measurement in terminal, save the following in simple.py:

.. code-block:: python

   from ambientco2 import Sensor

   serial_device = "/dev/ttyUSB0"
   sensor = Sensor(serial_device)

   co2 = sensor.read()["CO2"]

   print(co2)

and run the script:

.. code-block:: bash

   $ python3 ./simple.py
   $ 678
