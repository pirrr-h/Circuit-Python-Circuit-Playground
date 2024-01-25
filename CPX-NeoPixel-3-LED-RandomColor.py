import time
import board
import neopixel
import random

light = 0
r = 0
g = 0
b = 0
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

while True:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    light = random.randint(0, 9)
    pixels[light] = (r, g, b)
    time.sleep(0.01)
    