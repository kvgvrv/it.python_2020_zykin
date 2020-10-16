import turtle as tr 

def circle(n,R):
    for i in range(1,n+1):
        tr.pendown()
        tr.forward(R*3**0.5)
        tr.left(360/n)
    tr.right(90+180/n)
    tr.penup()
    tr.forward(15)
    tr.left(90+180/(n+1))
n = 10
tr.shape('turtle')
tr.speed(70)
R = 30
for i in range(3, n+1):
    circle(i,R)
    R+=15
