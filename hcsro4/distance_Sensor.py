"""
A skeleton program that i Usually start with.
"""
from signal import signal, SIGTERM, SIGHUP, pause
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

def execute():
    trig = 4
    echo = 18

    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

    GPIO.output(trig, True)
    time.sleep(0.001)
    
    GPIO.output(trig, False)
    
    while GPIO.input(echo) == False:
        start = time.time()
        
    while GPIO.input(echo) == True:
        end = time.time()
        
    sig_time = end - start
    
    distance = sig_time/0.000058 #cm , inches = sit_time / 0.000148
    print('Distance : {} cm'.format(distance))
    GPIO.cleanup()
        
execute()        

try:

    pause()

except KeyboardInterrupt:
    pass

finally:
    pass
