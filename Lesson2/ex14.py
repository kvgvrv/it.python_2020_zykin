import turtle as tr 
def star(n):
    for i in range(n):
        tr.forward(150)
        tr.left(180 - 360/2/n)
tr.shape('turtle')
tr.speed(10)
star(5)
tr.penup()
tr.goto(300,0)
tr.pendown()
star(11)
