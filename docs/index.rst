Python module for CozIR Ambient CO2 sensors
===========================================
The CozIR Ambient family of sensors all provide CO2 measurements, at different 
ranges. Some are able to measure temperature and relative humidity as well. 
The sensors use serial UART and analog voltage output.

Installation
============
    $ pip install ambientco2

Usage
=====
    from ambientco2 import Sensor
    
    serial_device = "/dev/ttyUSB0"    # Debian (Ubuntu, Raspberry Pi OS etc.)
    
    sensor = Sensor(serial_device)
    
    co2 = sensor.read()
    
    print(co2)
    
    >> 765

Module documentation
====================
.. automodule:: ambientco2.sensor
     :members:

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
