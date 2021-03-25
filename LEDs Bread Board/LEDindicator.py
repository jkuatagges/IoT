import RPi.GPIO as GPIO  #Import Pi GPIO Library
from time import sleep   #Import sleep function from time module

GPIO.setwarnings(False)  #Ignore warnings for now
GPIO.setmode(GPIO.BOARD) #use physical pin numbering(Not GPIO)
GPIO.setup(12,GPIO.OUT, initial = GPIO.LOW) #Set pin 7(GPIO 4) as both power and output, set initial value as low(Off)

while True:              #Run forever
    GPIO.output(12, GPIO.HIGH) #Turn on
    sleep(0.05)                # sleep(Go off) for 0.5 seconds
    
    GPIO.output(12, GPIO.LOW)  #Turn off
    sleep(0.05)                #sleep(Go off) for 0.5 seconds