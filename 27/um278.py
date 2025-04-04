import math
f = open('files/278.txt')
f.readline()

points = [list(map(float, s.replace(',','.').split())) for s in f]
cl = [[] for _ in range(3)]

for x, y in points:
    if y < -1:
        cl[0].append([x, y])
    elif y > -1 and x < 1:
        cl[1].append([x, y])
    else:
        cl[2].append([x, y])

best = [[] for _ in range(3)]

for i in range(len(cl)):
    mind = 10 ** 10
    for x1, y1 in cl[i]:
        sumd = 0
        for x2, y2 in cl[i]:
            sumd += math.dist([x1, y1], [x2, y2])
        if sumd < mind:
            mind = sumd
            best[i] = [x1, y1]

Px = int(sum([x for x, y in best])/len(cl) * 10000)
Py = int(sum([y for x, y in best])/len(cl) * 10000)
print(Px, Py)