import turtle
import math
bob = turtle.Turtle()
'''
bob.fd(25)
bob.bk(50)
bob.fd(25)
'''
def polygon (s,l,y):
    bob.penup()
    bob.sety(y)
    bob.pendown()
    angle = 360.0/s
    bob.fd(l/2)
    for i in range(0,s):
        if i != 0:
            bob.fd(l)
        bob.rt(angle)
    bob.fd(l/2)
#polygon(50,10,200)
def circle(d):
    n=d/16
    polygon(50,n,d/2)

#circle(360)


turtle.mainloop()
