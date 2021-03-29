"""
Description: This code demonstrates how to use Raspberry Pi to blink multiple patterns using multiple LEDs.  
"""

from signal import signal, SIGTERM, SIGHUP, pause #For safe running of continuos threading loops
from gpiozero import LED, Button                  #For safe running of continuos threading loops
from threading import Thread                      #For safe running of continuos threading loops
from time import sleep                            #For controling how fast or slow the pattern moves around
from random import randrange                      #For safe running of continuos threading loops

patterns = (
                [1, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [1, 1, 1, 1, 0, 0],
                [1, 1, 1, 1, 1, 0],
                [1, 0, 1, 0, 1, 0]
            )
#Assign the LEDs in and index are call them  using their numerical indices
#The numbers in bracket show GPIO pins, check the diagram in the images folder above
leds = (LED(4), LED(17), LED(27), LED(22), LED(13), LED(6))
button = Button(16)

is_running = True
delay = 0.1

index = 0
led_in = 5
led_out = 0

def safe_exit(signum, frame):
    exit(1)

def show_pattern():
    while is_running:
        for id in range(6):
            leds[id].value = patterns[index][id]

        token = patterns[index].pop(led_out)
        patterns[index].insert(led_in, token)

        sleep(delay)

def change_direction():
    global led_in, led_out, index

    led_in, led_out = led_out, led_in

    while True:
        new_index = randrange(0, len(patterns))

        if new_index != index:
            index = new_index
            break
try:

    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)

    button.when_pressed = change_direction
    index = randrange(0, len(patterns))

    worker = Thread(target=show_pattern, daemon=True)
    worker.start()

    pause()

except KeyboardInterrupt:
    pass

finally:
    is_running = False
    sleep(1.5*delay)

    for id in range(6):
        leds[id].close()
