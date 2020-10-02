import turtle
import numpy as np

turtle.shape('turtle')
R = 0.02
l = 2 * np.pi * R / 360
for j in range(3600):
       turtle.forward(2 * np.pi * R * j / 360)
       turtle.right(1)
   
