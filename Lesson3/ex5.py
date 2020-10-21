from random import randint, random
import turtle as tr

x_max, y_max = 300, 300
def space(t):
    tr.width(4)
    tr.goto(0, 0)
    tr.penup()
    tr.forward(x_max)
    tr.pendown()
    tr.right(90)
    tr.forward(y_max)
    tr.right(90)
    tr.forward(x_max*2)
    tr.right(90)
    tr.forward(y_max*2)
    tr.right(90)
    tr.forward(x_max*2)
    tr.right(90)
    tr.forward(y_max)
    tr.penup()
    tr.left(90)
    tr.goto(0, 0)
    tr.width(2)


number_of_turtles = 20
dt = 0.5

pool = [[tr.Turtle(shape='circle'), randint(-290, 290), randint(-290, 290), 
         randint(-20, 20), randint(-20, 20)]   for i in range(number_of_turtles)]

space(pool[0][0])

for unit in pool:
    unit[0].penup()
    unit[0].speed(0)
    unit[0].goto(unit[1], unit[2])
    unit[0].speed(10)
    
while True:
    for unit in pool:
        unit[1] += unit[3]*dt
        unit[2] += unit[4]*dt
        unit[0].goto(unit[1], unit[2])
        
        if abs(unit[2]) >= y_max:
            unit[4] *= -1
        if abs(unit[1]) >= x_max:
            unit[3] *= -1
