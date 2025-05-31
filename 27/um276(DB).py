# import math
# from timeit import dummy_src_name
#
# f = open('files/276a.txt')
# f.readline()
# points = [list(map(float, s.replace(',','.').split())) for s in f]
# clusters = []
# eps = 0.5
#
# while points:
#     clusters.append([points[0]])
#     del points[0]
#     for p1 in clusters[-1]:
#         for p2 in points[:]:
#             if  math.dist(p1, p2) < eps:
#                 clusters[-1].append(p2)
#                 points.remove(p2)
#     if len(clusters[-1]) <= 10:
#         del clusters[-1]
#
# best = [[] for i in range(len(clusters))]
# for i in range(len(clusters)):
#     mind = 10 ** 10
#     for x1, y1 in clusters[i]:
#         sumd = 0
#         for x2, y2 in clusters[i]:
#             sumd += math.dist([x1, y1], [x2, y2])
#         if sumd < mind:
#             mind = sumd
#             best[i] = [x1, y1]
#
# px = sum([x for x, y in best]) / len(best)
# py = sum([y for x, y in best]) / len(best)
# pxy = int((px + py) * 10_000)
#
# ps = int(sum([len(i) / 16 for i in clusters]) * 1000)
# print(pxy, ps)

####B####
import math


f = open('files/276b.txt')
f.readline()
p = [list(map(float, s.replace(',','.').split())) for s in f]
clusters = []
eps = 0.2

while p:
    clusters.append([p[0]])
    del p[0]
    for p1 in clusters[-1]:
        for p2 in p[:]:
            if math.dist(p1, p2) < eps:
                clusters[-1].append(p2)
                p.remove(p2)
    if len(clusters[-1]) <= 10:
        del clusters[-1]

k = 3
best = [[] for i in range(k)]
for i in range(k):
    mind = 10**10
    for x1, y1 in clusters[i]:
        sumd = 0
        for x2, y2 in clusters[i]:
            sumd += math.dist([x1, y1], [x2, y2])
        if sumd < mind:
            mind = sumd
            best[i] = [x1, y1]

px = sum([x for x, y in best]) / len(best)
py = sum([y for x, y in best]) / len(best)
pxy = int((px + py) * 10_000)
ps = int(sum([len(i) / 16 for i in clusters]) * 1000)
print(pxy, ps)

