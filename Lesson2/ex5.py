import turtle


turtle.shape('turtle')
a = 5
x = 10
for i in range (10):
    for j in range (4):
        turtle.forward(a + 2 * x * i)
        turtle.right(90)
    turtle.penup()
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.pendown()
    turtle.left(180)
