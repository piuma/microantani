from microbit import *
import random

display.scroll('Roll the dice!')
while True:
    if accelerometer.was_gesture("shake"):
        display.clear()
        display.show(str(random.randint(1, 6)))
    sleep(20)
    
