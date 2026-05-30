# Imports go at the top
from microbit import *

x = 2
y = 2

def flash(n):
    display.clear()
    for i in range(n):
        for bright in range(10):
            for row in range(5):
                for col in range(5):
                    display.set_pixel(row,col,bright)
            sleep(30)
        for bright in range(10):
            for row in range(5):
                for col in range(5):
                    display.set_pixel(row,col,9-bright)
            sleep(30)

flash(3)

# main loop
while True:
    x = x + accelerometer.get_x()/30000
    if x > 4:
        x = 4
    if x < 0:
        x = 0
    y = y + accelerometer.get_y()/30000
    if y > 4:
        y = 4
    if y < 0:
        y = 0
    #display.clear()
    display.set_pixel(int(x),int(y),9)
