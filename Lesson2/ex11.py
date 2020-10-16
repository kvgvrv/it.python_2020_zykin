import turtle as tr
import numpy as np

def circle_right(R):
    tr.shape('turtle')
    l = 2 * np.pi * R / 180
    for i in range(180):
        tr.forward(l)
        tr.right(2)
        
def circle_left(R):
    tr.shape('turtle')
    l = 2 * np.pi * R / 180
    for i in range(180):
        tr.forward(l)
        tr.left(2)
        
R = 15        
for i in range(10):      
    circle_right(R)
    circle_left(R)
    R+=5
    
