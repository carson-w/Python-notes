import turtle
bob = turtle.Turtle()
bob.penup()
bob.sety(200)
bob.pendown()
def polygon (s,l):
    angle = 360.0/s
    for i in range(0,s):
        bob.fd(l)
        bob.rt(angle)
polygon(6,300)
