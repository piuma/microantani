from microbit import *

SECRET_CODE='ABBA'

display.show(Image.CONFUSED)

INPUT_CODE=''

while (len(INPUT_CODE) < 4):
    if button_a.is_pressed():
        INPUT_CODE = INPUT_CODE + 'A'
        sleep(1000)
    elif button_b.is_pressed():
        INPUT_CODE = INPUT_CODE + 'B'
        sleep(1000)
    sleep(10)

display.clear()

if SECRET_CODE == INPUT_CODE:
    display.show(Image.HAPPY)
else:
    display.show(Image.SAD)
