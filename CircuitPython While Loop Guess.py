import time
import random
import neopixel
import board
i = 0
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

print("enter the number 0-10")
answer = int(input())

if (answer >= 0) and (answer <= 10):
    i = 1
    pixels[answer] = (0, 255, 0)
if (i == 1):
    x = 0
    while (x <= 4):
        guess = random.randint(0,10)
        if guess == answer:
            pixels[guess] = (0, 0, 255)
            print("I guessed", guess, "I got it right!")
            break
        elif guess != answer:
            pixels[guess] = (255, 0, 0)
            print("I guessed", guess, "I got it wrong :(")
            x = x + 1
            time.sleep(0.8)
        
        
            


