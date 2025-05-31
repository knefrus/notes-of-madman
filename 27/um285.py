f = open('files/285.txt')
f.readline()
import math
p = [list(map(float, s.replace(',','.').split())) for s in f]
cl = [[] for _ in range(2)]

for x,y in p:
    if x > 0 and y > 0:
        cl[1].append([x, y])
    else:
        cl[0].append([x, y])

b = [[] for _ in range(2)]

for i in range(2):
    mind = 10 ** 10
    for p1 in cl[i]:
        c = 0
        for p2 in cl[i]:
            c += math.dist(p1, p2)
        if c < mind:
            mind = c
            b[i] = [p1]

Px = 
