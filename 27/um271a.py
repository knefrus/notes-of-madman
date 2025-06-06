f = open('files/27A217.txt')
f.readline()
points = [list(map(float, i.replace(',', '.').split()))for i in f]

clusters = [[], []]

for x, y in points:
    if x > 0:
        clusters[1].append([x, y])
    else:
        clusters[0].append([x, y])


best = [[], []]

for i in range(len(clusters)):
    min = 10 ** 10
    for x1, y1 in clusters[i]:
        sumd = 0
        for x2, y2 in clusters[i]:
            d = ( (x2 - x1) ** 2 + (y2 - y1) ** 2 )**0.5
            sumd += d
        if sumd < min:
            min = sumd
            best[i] = [x1, y1]

px = int( (sum([x for x, y in best]) / len(best)) * 10000)
py = int( (sum([y for x, y in best]) / len(clusters)) * 10000)

print(px, py)