# colorwheelADC.py:  Shows all the colors of the rainbow on the NeoPixel LEDs
#                    The ADC is used to choose the angle on the color wheel
# 
# Copyright U. Raich 2022
# The program is part of African School of Physics 2022
# Released under the MIT license

import sys
from utime import sleep_ms
from machine import Pin,ADC
from neopixel import NeoPixel


# We set the max LED intensity to 31 in order not to blind our eyes
MAX_INTENSITY = 31
NEOPIXEL_PIN = 26
NO_OF_LEDS   = 7

# these are the color components (used only for printing)
RED = 0
GREEN = 1
BLUE = 2

dark = (0,0,0)

# clears all the LEDs
# this is used to switch off all the LEDs when we terminate the program with ^C
def clear():
    # clear all the LEDs
    for i in range(NO_OF_LEDS):
        neopixel[i]=dark
        neopixel.write()

# init the NeoPixel driver
neopixel = NeoPixel(Pin(NEOPIXEL_PIN),NO_OF_LEDS)

# init the linear potentiometer
slider = ADC(Pin(36),atten=ADC.ATTN_11DB)  # create ADC object on ADC pin 36

# if you observe the color wheel very attentively then you see that there is only one color component that
# is changing as we go around the ring.
# 0°..60°:     red is constantly at max, blue is constantly zero and green increases
# 60°.. 120°:  green is constantly at max, blue is zero and red decreases
# similar for all the 6 sectors
# We must therefore check in which sector the angular position is falling, then we can easily calculate
# the color components depending on the angular position around the ring

def colors(pos):
    if pos<60:
        red=MAX_INTENSITY
        green=int(MAX_INTENSITY*pos/60)
        blue=0
    elif pos >=60 and pos < 120:
        red=MAX_INTENSITY-int(MAX_INTENSITY*(pos-60)/60)
        green = MAX_INTENSITY
        blue = 0
    elif pos >=120 and pos < 180:
        red = 0
        blue = int(MAX_INTENSITY*(pos-120)/60)
        green = MAX_INTENSITY
    elif pos >= 180 and pos < 240:
        red = 0
        green = MAX_INTENSITY-int(MAX_INTENSITY*(pos-180)/60)
        blue = MAX_INTENSITY
    elif pos >= 240 and pos < 300:
        red = int(MAX_INTENSITY*(pos-240)/60)
        green = 0
        blue = MAX_INTENSITY
    else:
        red = MAX_INTENSITY
        green = 0
        blue = MAX_INTENSITY - int(MAX_INTENSITY*(pos-300)/60)

    return (red,green,blue)
             

def show(color):
    for i in range(NO_OF_LEDS):
        neopixel[i] = color
    neopixel.write()

def print_colors(color):
    print("red: {:03d}, green: {:03d}, blue: {:03d}".format(color[RED],color[GREEN],color[BLUE]))
        
print("ADC color wheel running on ",sys.platform)

printFlag = True
# First we read the slider and map its value from the 0..4095 range to 0..360
# Then we use this angle to find the corresponding color on the color wheel

try:
    while True:
        # read the slider
        pos = int(slider.read() * 360.0 / 4095)
        print ("Color position: ",pos)
        show(colors(pos))
        sleep_ms(100)
except KeyboardInterrupt:
    clear()
            
