from turtle import *
left(90)
k = 40
pendown()
for i in range(9):
    right(80)
    forward(k * 5)

penup()
for x in range(-10, 10):
    for y in range(-10, 10):
        setpos(x * k , y * k)
        dot(4)

done()

#otvet 9