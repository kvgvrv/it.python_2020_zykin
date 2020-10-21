import turtle as tr


tr.shape('circle')

x = -450
y = 0
Vx = 20
Vy = 50
t = 0
g = -10

tr.width(4)
tr.forward(450)
tr.goto(x,y)
tr.width(2)
for i in range (1, 10000):
    tr.speed(0.001 * (Vx**2 + Vy**2)**0.5)
    t = i / 100
    x += Vx * t
    y += Vy * t + (g / 2) * t**2
    Vy += g * t
    if ( y >= 0): 
        tr.goto(x,y)
    else:
        Vy -= g * t
        Vy = 0.9 * abs(Vy)
        x -= Vx * t / 2
        y = 0
        tr.goto(x,y)
