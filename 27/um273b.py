import math as m

f = open('files/273b.txt')
f.readline()
k = 3

points = [ list(map(float, i.replace(',','.').split())) for i in f ]
clusters = [[] for i in range(k)]
mids = [[] for i in range(k)]

for x, y, br in points: #кластеризация
    if y > 0:
        clusters[0].append([x,y,br])
    elif x < 0.5:
        clusters[1].append([x,y,br])
    else:
        clusters[2].append([x, y, br])

for i in range(k): #поиск центров
    min_dist = 10**10
    for x1, y1, br1 in clusters[i]:
        sum_dist = 0
        for x2, y2, br2 in clusters[i]:
            sum_dist += m.dist([x1, y1], [x2, y2])
        if sum_dist < min_dist:
            min_dist = sum_dist
            mids[i] = [x1, y1, br1]

sbr = []
for i in range(k): #средняя яркость
    sbr1 = 0
    for x, y, br in clusters[i]:
        sbr1 += br
    sbr.append(sbr1 / len(clusters[i]))


P_xy = int(sum([x + y for x, y, br in mids]) * 10000)
P_m = int(sum(sbr) * 1000)

print(P_xy, P_m)