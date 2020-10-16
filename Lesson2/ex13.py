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
        
def half_circle_right(R):
    tr.shape('turtle')
    l = 2 * np.pi * R / 180
    for i in range(90):
        tr.forward(l)
        tr.right(2)
        
def eye(l):
    tr.left(45)
    tr.forward(l)
    tr.right(90)
    tr.forward(l)
    tr.left(45)
        
tr.begin_fill()
tr.color('black', 'yellow')
circle_right(120)
tr.end_fill()
tr.penup()
tr.goto(-60, -80)
tr.pendown()
eye(30)
tr.penup()
tr.goto(30, -80)
tr.pendown()
eye(30)
tr.penup()
tr.goto(-50, -180)
tr.pendown()
tr.right(90)
half_circle_left(25)
tr.right(180)
half_circle_left(25)
tr.penup()
tr.goto(0, -100)
tr.pendown()
tr.right(180)
tr.forward(40)
tr.right(180)
tr.penup()
tr.goto(-60,-120)
tr.pendown()
tr.color('pink', 'pink')
tr.begin_fill()
circle_right(10)
tr.end_fill()
tr.penup()
tr.goto(40, -120)
tr.pendown()
tr.begin_fill()
circle_right(10)
tr.end_fill()


