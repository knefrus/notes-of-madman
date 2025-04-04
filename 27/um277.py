import math
f = open('files/277.txt')
f.readline()
points = [list(map(float, s.replace(',','.').split())) for s in f]
cl = [[] for _ in range(3)]
for x,y in points:
    if x > -1:
        cl[2].append([x, y])
    elif y > 0:
        cl[1].append([x, y])
    else:
        cl[0].append([x, y])
best = [[], [], []]
for i in range(3):
    mind = 10 ** 10
    for x1, y1 in cl[i]:
        sumd = 0
        for x2, y2 in cl[i]:
            dist = math.dist([x1, y1], [x2, y2])
            sumd += dist
        if sumd < mind:
            mind = sumd
            best[i] = [x1, y1]
Px = int(sum([x for x, y  in best])/3*10_000)
Py = int(sum([y for x, y  in best])/3*10_000)
print(Px, Py)