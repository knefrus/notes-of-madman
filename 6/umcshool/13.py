from turtle import *
tracer(1)
left(90)
k = 50
for i in range(24):
    right(90)
    forward(k)
    left(45)
    backward(k)

penup()
for x in range(-10, 10):
    for y in range(-10, 10):
        setpos(k * x, k * y)
        dot(4)

#3 otvet