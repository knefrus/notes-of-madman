from idlelib.squeezer import count_lines_with_wrapping
from xxsubtype import bench

f = open('27A272.txt')
f.readline()

points = [ list(map(float, s.replace(',', '.').split())) for s in f]

clusters = [ [], [] ]

for x, y in points:
    if x > -4:
        clusters[1].append([x, y])
    else:
        clusters[0].append([x, y])

goidaZ = [[], []]

for i in range(len(clusters)):
    mind = 10 ** 10
    for x1, y1 in clusters[i]:
        sumd = 0
        for x2, y2 in clusters[i]:
            d = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
            sumd += d
        if sumd < mind:
            mind = sumd
            goidaZ[i] = [x1, y1]

ZOVx = int( sum([x for x,y in goidaZ]) / len(goidaZ) * 10_000 )
ZOVy = int(sum([y for x, y in goidaZ]) / len(goidaZ) * 10_000)

print(ZOVx, ZOVy)