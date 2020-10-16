import turtle as tr
import numpy as np

def circle_right():
    tr.shape('turtle')
    R = 100
    l = 2 * np.pi * R / 360
    for i in range(360):
        tr.forward(l)
        tr.right(1)
        
def circle_left():
    tr.shape('turtle')
    R = 100
    l = 2 * np.pi * R / 360
    for i in range(360):
        tr.forward(l)
        tr.left(1)
for i in range(4):      
    circle_right()
    circle_left()
    tr.right(180/4)
