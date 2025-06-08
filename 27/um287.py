from math import *
k = 2
data = []
for s in open('files/287.txt'):
    x,y = [float(d) for d in s.replace(',','.').split()]
    data.append([x,y])

cl = []
while data:
    prob = [data.pop()]
    for p in prob:
        ss = [p1 for p1 in data if dist(p1, p)<1]
        for p1 in ss:
            prob.append(p1)
            data.remove(p1)
    if len(prob) > 30:
        cl.append(prob)

print([len(q1) for q1 in cl])

def pl(cl1):
    m = []
    k = len(cl1)
    for p in cl1:
        for p1 in cl1:
            if dist(p1, p) <= 1:
                k +=1
        m.append()