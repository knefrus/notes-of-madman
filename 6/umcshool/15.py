from turtle import *
left(90)
k = 30

for i in range(3):
    forward(k * 10)
    right(120)

penup()

for x in range(0, 11):
    for y in range(0, 11):
        setpos(k * x, k * y)
        dot(4)

#38 otvet