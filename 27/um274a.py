import math as m
f = open('files/274a.txt')
f.readline()
k = 2

points = [list(map(float, i.replace(',','.').split())) for i in f]
mids = [[] for _ in range(k)]
clusters = [[] for _ in range(k)]

for x, y, br in points: #кластеризация
    if x > 0:
        clusters[0].append([x, y, br])
    else:
        clusters[1].append([x, y, br])

for i in range(k): #центроиды
    min_dist = 10**10
    for x1, y1, br1 in clusters[i]:
        sum_dist = 0
        for x2, y2, br2 in clusters[i]:
            sum_dist += m.dist([x1, y1], [x2, y2])
        if sum_dist < min_dist:
            min_dist = sum_dist
            mids[i] = [x1, y1, br1]

P_xy = int(sum([x + y for x,y,br in mids]) * 10000)


sr = [] #средние значения яркости
for x in range(k):
    srz = 0
    for x, y, br in clusters[i]:
       srz += br
    sr.append(srz/len(clusters[i]))



disp = [] #отклонения
for i in range(k): #дисперсия яркости
    di = 0
    for x, y, br in clusters[i]:
        di += (br - sr[i]) ** 2
    disp.append((di / len(clusters[i])) ** 0.5)

os = []
for i in range(k):
    kolvo = 0
    for x, y, br in clusters[i]:
        if br/sr[i] > (1.5*(disp[i])):
            kolvo += 1
    os.append(kolvo)

P_n = int(sum(os))
print(P_xy, P_n)