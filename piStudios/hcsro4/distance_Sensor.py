"""
HCSRO4 ultrasonic Distance sensor
"""
from signal import signal, SIGTERM, SIGHUP, pause
import RPi.GPIO as GPIO
from time import sleep
from threading import Thread
from gpiozero import DistanceSensor as dists
GPIO.setwarnings(False)

reading = True
sensor = dists(echo = 18, trigger = 4)

def safe_exit(signum, frame):
    exit(1)

def read_distance():
    while reading:
        print("Distance: "+'{:1.2f}'.format(sensor.value) + " m")
        sleep(1)
        
signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)

try:
    reader = Thread(target = read_distance, daemon = True)
    reader.start()
    
    pause()

except KeyboardInterrupt:
    pass

finally:
    reading = False
    sensor.close()

