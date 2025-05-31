#P.s я не пидорас, попробовать переборное решение решил по приколу
import math
f = open('files/282.txt')
f.readline()
p = [list(map(float, s.replace(',','.').split())) for s in f]
best = [[], []]
mind = 10 ** 10
for i in range(len(p)-1):
    for j in range(i + 1, len(p)):
        c1 = p[i]
        c2 = p[j]
        sumd = 0
        for poi in p:
            d1 = math.dist(c1, poi)
            d2 = math.dist(c2, poi)
            sumd += min(d1, d2)
        if sumd < mind:
            mind = sumd

            best = [c1, c2]

px = int(sum([x for x, y in best])/len(best) * 10000)
py = int(sum([y for x, y in best])/len(best) * 10000)
print(px, py)
