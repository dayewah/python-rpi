from time import sleep
from sense_hat import SenseHat
from random import randint
sense=SenseHat()


x,y=0,0
a,b=1,1

vertical=True
while True:
    sleep(0.1)
    r=randint(1,255)
    g=randint(1,255)
    bl=randint(1,255)
    # Define some colours
    w = (r,g,bl) # White
    sense.clear()
        
    if vertical:
        y+=a
        print("vertical "+str(x) +" " +str(y)) 
        if y==0:
            a=1
            vertical=False
        if y==7:
            a=-1
            vertical=False
        
    else:
        x+=b
        print("horizontal "+str(x) +" " +str(y)) 
        if x==0:
            b=1
            vertical=True
        if x==7:
            b=-1
            vertical=True
        
    # move
    sense.set_pixel(x,y,w)
        
        
           
        
        
    
