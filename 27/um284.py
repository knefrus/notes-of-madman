import math
f = open('files/284.txt')
f.readline()
p = [list(map(float, s.replace(',','.').split())) for s in f]
k = 4
cl = [[] for _ in range(k)]

for x, y in p:
    if y > 4:
        cl[0].append([x, y])
    elif x > 2:
        cl[1].append([x, y])
    elif x < -4:
        cl[2].append([x, y])
    else:
        cl[3].append([x, y])

del cl[cl.index(max(cl, key=len))]

centr = [[] for _ in range(k-1)]

for i in range(len(cl)):
    mind = 10 ** 10
    for x1,y1 in cl[i]:
        sumd = 0
        for x2, y2 in cl[i]:
            sumd += math.dist([x1, y1], [x2, y2])
        if sumd < mind:
            mind = sumd
            centr[i] = [x1, y1]
print(centr)
xx = int(sum([x for x,y in centr]) / 3 * 10_000)
yy = int(sum([y for x,y in centr]) / 3 * 10_000)
print(xx, yy)