import math

f = open('files/273a.txt')
k = 2
points = [list(map(float, s.replace(',', '.').split()))for s in f]
clusters = [[] for _ in range(k)]

for x, y, bright in points:
    if x < -1:
        clusters[0].append([x, y, bright])
    else:
        clusters[1].append([x, y, bright])

best =[[] for _ in range(k)]

for i in range(len(clusters)):
    min_clust = 10 ** 10
    for x1, y1, bright1 in clusters[i]:
        sum_dist = 0
        for x2, y2, bright2 in clusters[i]:
            sum_dist += math.dist([x1, y1], [x2, y2])
        if sum_dist < min_clust:
            min_clust = sum_dist
            best[i] = [x1, y1, bright1]
s1 = 0
s_k = []
for i in range(len(clusters)):
    for x, y, bright in clusters[i]:
        s1 += bright
    s1 = s1 / len(clusters[i])
    s_k.append(s1)

P_xy = sum([x + y for x, y, bright in best]) * 10000
print(int(P_xy))
print(int(sum(s_k) * 1000))
