from time import sleep
from sense_hat import SenseHat
sense=SenseHat()

on=False
x=0
y=0
while True:
    sleep(0.1)
    on= not on
    if on:
        r=0
        g=0
        b=0
        sense.clear((r,g,b))
    else:
        # Define some colours
        w = (255, 255, 255) # White
        b = (0, 0, 0) # Black

        # Set up where each colour will dis
        creeper_pixels = [
            b, b, b, b, b, b, b, b,
            b, b, b, b, b, b, b, b,
            b, b, b, b, b, b, b, b,
            b, b, b, b, b, b, b, b,
            b, b, b, b, b, b, b, b,
            b, b, b, b, b, b, b, b,
            b, b, b, b, b, b, b, b,
            b, b, b, b, b, b, b, b
        ]

        # Display these colours on the LED matrix
        sense.set_pixels(creeper_pixels)
        
        # move
        sense.set_pixel(x,y,w)
        x+=1
        y+=1
        if x==8: x=0
        if y==8: y=0
        
        
        
    
