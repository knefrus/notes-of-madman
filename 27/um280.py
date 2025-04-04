f = open('files/280.txt')
f.readline()
import math
points = [list(map(float, s.replace(',','.').split())) for s in f]

cl = [[],[]]
best = [[],[]]

for x, y in points:
    if x > 1.5:
        cl[1].append([x, y])
    else:
        cl[0].append([x, y])

for i in range(2):
    mind = 10 ** 10
    for x1, y1 in cl[i]:
        sumd = 0
        for x2, y2 in cl[i]:
            sumd += math.dist([x1,y1], [x2,y2])
        if sumd < mind:
            mind = sumd
            best[i] = [x1, y1]

px = sum([x for x,y in best]) / 2
py = sum([y for x,y in best]) / 2
print(int((px + py) * 10000))
print(len(cl[0]) / 16 + len(cl[1]) / 16)