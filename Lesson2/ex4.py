import turtle
import numpy as np

turtle.shape('turtle')
R = 100
l = 2 * np.pi * R / 360
for i in range(360):
    turtle.forward(l)
    turtle.right(1)
