# import math
# f = open('files/275a.txt')
# f.readline()
# k = 2
# points = [list(map(float, s.replace(',','.').split())) for s in f]
# clusters = []
# eps = 0.5
#
# while points:
#     clusters.append([points[0]])
#     del points[0]
#     for p1 in clusters[-1]:
#         for p2 in points[:]:
#             if math.dist(p1, p2) < eps:
#                 clusters[-1].append(p2)
#                 points.remove(p2)
#
# best = [[] for i in range(k)]
# for i in range(k):
#     min_dist = 10 ** 10
#     for x1, y1 in clusters[i]:
#         sum_dist = 0
#         for x2, y2 in clusters[i]:
#             sum_dist += math.dist([x1, y1], [x2, y2])
#         if sum_dist < min_dist:
#             min_dist = sum_dist
#             best[i] = [x1, y1]
# sx = 0
# sy = 0
# for x, y in best:
#     sx += x
#     sy += y
# P_x = int( sx / len(best) * 10_000)
# P_y = int( sy / len(best) * 10_000)
# print(P_x, P_y)

import math
from turtle import *

f = open('files/275b.txt')
f.readline()
points = [list(map(float, s.replace(',','.').split())) for s in f]
clusters = []
eps = 0.5

while points:
    clusters.append([points[0]])
    del points[0]
    for p1 in clusters[-1]:
        for p2 in points[:]:
            if math.dist(p1, p2) < eps:
                clusters[-1].append(p2)
                points.remove(p2)

best = [[] for i in range(len(clusters))]
for i in range(len(clusters)):
    min_dist = 10**10
    for x1, y1 in clusters[i]:
        sum_dist = 0
        for x2, y2 in clusters[i]:
            sum_dist += math.dist([x1, y1], [x2, y2])
        if sum_dist < min_dist:
            min_dist = sum_dist
            best[i] = [x1, y1]

sx=0
sy=0
for x,y in best:
    sx += x
    sy += y
P_x = int(sx / len(best) * 10_000)
P_y = int(sy / len(best) * 10_000)
print(P_x, P_y)