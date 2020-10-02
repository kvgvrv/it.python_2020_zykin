import turtle
import numpy as np

turtle.shape('turtle')
R = 0.02
l = 2 * np.pi * R / 360
for j in range(3600):
    for i in range(1):
        turtle.forward(2 * np.pi * R * j / 360)
        turtle.right(1)
   
