from turtle import *
tracer(0)
left(90)
right(45)
k = 30
forward(k * 4)
for i in range(10):
    right(45)
    forward(7 * k)
    right(135)
    forward(4 * k)

penup()
for x in range(-10, 10):
    for y in range(-10, 10):
        setpos(k * x, k * y)
        dot(3)
done()
#12 otvet 