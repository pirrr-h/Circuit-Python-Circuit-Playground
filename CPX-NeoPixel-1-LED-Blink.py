
import time
import board
import neopixel

# Calls the circuit Python neopixel library, specifies the default board 
# pins for the Neopixels, and the number of neopixels to access.  Returns a 
# list 'pixels' of indexable neopixles
pixels = neopixel.NeoPixel(board.NEOPIXEL, 2)

while True:
    pixels[0] = (0, 255, 0)
    time.sleep(0.5)
    pixels[1] = (6, 3, 0)
    time.sleep(0.5)
    pixels[1] = (255, 0, 0)