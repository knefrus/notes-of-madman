import math as m
f = open('files/274a.txt')
f.readline()
k = 3

p = [list(map(float, i.replace(',','.').split())) for i in f]
cl = [[] for _ in range(k)]
bst = [[] for _ in range(k)]

for x, y, br in p:
    if x > 0:
        cl[2].append([x,y,br])
    elif y < 0:
        cl[1].append([x,y,br])
    else:
        cl[0].append([x,y,br])


for i in range(k):
    mind = 10 ** 10
    for x1, y1, br1 in cl[i]:
        sumd = 0
        for x2, y2, br2 in cl[i]:
            sumd += m.dist([x1, y1], [x2, y2])
        if sumd < mind:
            mind = sumd
            bst[i] = [x1, y1, br1]

P_xy = int(sum([x + y for x,y,br in bst]) * 10000)

sra = []
for i in range(k):
    sr = 0
    for x, y, br in cl[i]:
        sr += br