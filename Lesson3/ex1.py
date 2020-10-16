import turtle as tr 
from random import *

tr.shape('turtle')
tr.speed(10)
tr.width(3)
tr.color('red')
for i in range(randint(1,100)):
    tr.forward(randint(1,200))
    tr.right(randint(0,360))
    
