from turtle import *
left(90)
k = 30

for i in range(2):
    forward(k * 13)
    right(90)
    forward(k * 5)
    right(90)


penup()
for x in range(0, 15):
    for y in range(0, 15):
        setpos(k * x, y * k)
        dot(4)
#65 otvet