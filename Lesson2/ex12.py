import turtle as tr
import numpy as np

def half_circle_right(R):
    tr.shape('turtle')
    l = 2 * np.pi * R / 180
    for i in range(90):
        tr.forward(l)
        tr.right(2)
        
R = 50
r = 15
tr.left(90)        
for i in range(10):      
    half_circle_right(R)
    half_circle_right(r)

    
