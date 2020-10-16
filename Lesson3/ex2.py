import turtle as tr
def draw(A):
    for i in range(len(A[0])):
            tr.right(A[0][i])
            tr.forward(A[1][i])

digits = [[(90,270,270,270), (80,40,80,40)],[(225,135), (40*2**0.5,80)],[],[],[(90,270,270,180), (40,40,40,80)],[],[],[(0,135,315),(40,40*2**0.5,40)]]
index = (1,4,1,7,0,1)

for i, n in enumerate(index):
    if n == 1:
        tr.penup()
        tr.right(90)
        tr.forward(40)
        tr.pendown()
        draw(digits[n])
        tr.penup()
        tr.goto(80+80*i, 0)
        tr.pendown()
        tr.left(90)
    else:
        draw(digits[n])
        tr.penup()
        tr.goto(80+80*i, 0)
        tr.pendown()
        if n == 0:
            tr.left(180)
        if n == 4:
            tr.left(90)
        if n == 7:
            tr.left(90)
