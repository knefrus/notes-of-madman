f = open('files/283.txt')
f.readline()
import math
points = [list(map(float, s.replace(',','.').split())) for s in f]
cl = [[], [], [], [], []]

for x, y in points:
    if y > 0.5 and x < 2.4:
        cl[0].append([x, y])
    elif y > 0.5 and x > 2.4:
        cl[1].append([x, y])
    elif y < -2.2 and x > -3:
        cl[4].append([x, y])
    elif y < 0.2 and y > -2 and x < 2 and x > -3:
        cl[2].append([x, y])
    else:
        cl[3].append([x, y])

del(cl[1])
best = [[],[],[],[]]
for i in range(4):
    mind = 10 ** 10
    for x1, y1 in cl[i]:
       sumd = 0
       for x2, y2 in cl[i]:
           sumd += math.dist([x1, y1], [x2, y2])
       if sumd < mind:
          mind = sumd
          best[i] = [x1, y1]

xx = int(sum([x for x, y in best]) / 4 * 10000)
yy = int(sum([y for x, y in best]) / 4 * 10000)
print(xx, yy)