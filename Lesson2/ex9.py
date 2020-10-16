import turtle as t 

def mnog(n,R):
    for i in range(1,n+1):
        t.pendown()
        t.forward(R*3**0.5)
        t.left(360/n)
    t.right(90+180/n)
    t.penup()
    t.forward(15)
    t.left(90+180/(n+1))
n = 10
t.shape('turtle')
t.speed(70)
R = 30
for i in range(3, n+1):
    mnog(i,R)
    R+=15
