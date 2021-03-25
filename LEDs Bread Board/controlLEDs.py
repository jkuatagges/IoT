import RPi.GPIO as GPIO
import time #to delay your LED

#Set up your pins to use board numbering
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

ledPin = 16 #GPIO 23

#Set pin 16(GPIO 23) as both power and output, set initial value as low(Off)
GPIO.setup(ledPin, GPIO.OUT, initial = GPIO.LOW)

#Flashing
def flashYllw():
    while True: #Run forever
        print("Turning on")
        GPIO.output(ledPin, GPIO.HIGH)
        time.sleep(0.09)
        print("Going Off")
        GPIO.output(ledPin, GPIO.LOW)
        time.sleep(0.09)
     
flashYllw()  
