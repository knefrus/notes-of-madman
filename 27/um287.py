import math
f = open('files/287.txt')
f.readline()
p = [list(map(float, s.replace(',','.').split())) for s in f]
k = 2
cl = [[] for _ in range(k)]
b = [[] for _ in range(k)]

for x, y in p:
    if x < -2:
        cl[0].append([x, y])
    else:
        cl[1].append([x, y])
for n in range(k):
    md = 10 ** 10
    for p1 in cl[n]:
        sd = 0
        for p2 in cl[n]:
            sd += math.dist(p1, p2)
        if sd < md:
            md = sd
            b[n] = p1

Px = abs(int(sum([x for x, y in b]) / k * 10000))
Py = abs(int(sum([y for x, y in b]) / k * 10000))
print(Px, Py)