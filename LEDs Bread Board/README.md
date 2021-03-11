### Explanation of the Code
`ONandOFF.py`
This is a step by step explanation of how the code works
#### Built With
- Raspberry PI
- Jumper wires
- LED
- Breadboard(Optional)
- 

`import RPi.GPIO as GPIO`

The first line tells the Python interpreter (the thing that runs the Python code) that it will be using a ‘library’ that will tell it how to work with the Raspberry Pi’s GPIO pins.

`import time`

The [time python library](https://pypi.org/project/time/) is used when doing anythin time-dependant.
e.g turn our LED after some time then off after some time again, on and off, timely.

`GPIO.setmode(GPIO.BCM)`

Each GPIO pin on the Raspberry Pi has several different names, so set mode to tell the program which naming convention is to be used.Here we're using the [GPIO.BCM](https://raspi.tv/2013/rpi-gpio-basics-4-setting-up-rpi-gpio-numbering-systems-and-inputs)
