f = open('files/27B272.txt')
f.readline()

points = [list(map(float, s.replace(',','.').split())) for s in f]

clusters = [[],[],[]]

for x,y in points:
    if x < -4:
        clusters[0].append([x, y])
    elif y > 2:
        clusters[1].append([x, y])
    else:
        clusters[2].append([x, y])

best = [[],[],[]]

for i in range(len(clusters)):
    mind = 10**10
    for x1, y1 in clusters[i]:
        sumd = 0
        for x2, y2 in clusters[i]:
            d = ((x2-x1) ** 2 + (y2-y1) ** 2) ** 0.5
            sumd += d
        if sumd < mind:
            mind = sumd
            best[i] = [x1, y1]

px = int( sum([x for x, y in best]) / len(best) * 10_000)
py = int(sum([y for x, y in best]) / len(best) * 10_000)
print(px, py)