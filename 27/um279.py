f = open('files/279.txt'); f.readline(); import math; points = [list(map(float, s.replace(',','.').split())) for s in f]; cl = [[],[],[]]
for x,y in points:
    if x < -1:cl[0].append([x, y])
    elif y > 0 and x > 0:cl[1].append([x, y])
    else:cl[2].append([x, y])
centr = [[], [], []]
for i in range(3):
    mind = 10 ** 10
    for x1, y1 in cl[i]:
        sumd = 0
        for x2, y2 in cl[i]:dist = math.dist([x1, y1],[x2, y2]); sumd += dist
        if sumd < mind: mind = sumd; centr[i] = [x1, y1]
print(centr); Px = int(sum([x for x, y in centr]) / 3 * 10_000); Py = int(sum([y for x, y in centr]) / 3 * 10_000); print(Px, Py)