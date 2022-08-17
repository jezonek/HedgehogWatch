# HedgehogWatch
Small script for displaying date and time using Raspberry Pi and max7219 7-segment display module

## Requirements
To run script you need max7219 library. It's available on pypi:
`pip install max7219`

## Connection
GPIO pin-outs
-------------

The breakout board has two headers to allow daisy-chaining:


============ ====== ============= ========= ====================
Board Pin    Name   Remarks       RPi Pin   RPi Function
------------ ------ ------------- --------- --------------------
1            VCC    +5V Power     2         5V0
2            GND    Ground        6         GND
3            DIN    Data In       19        GPIO 10 (MOSI)
4            CS     Chip Select   24        GPIO 8 (SPI CE0)
5            CLK    Clock         23        GPIO 11 (SPI CLK)
============ ====== ============= ========= ====================

That connection diagram is copied from max7219 repo.
To 
