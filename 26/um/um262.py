#n занятых
#m рядов
#k мест
f = open('files/um262.txt')
n, m, k = map(int, f.readline().split())

menfo = [[] for i in  range(k+1)]

for i in f:
    ryad, mesto = map(int, i.split())
    menfo[mesto].append(ryad)

res = []
for i in range(1, len(menfo)):
    menfo[i] = sorted([0] + menfo[i] + [m + 1], reverse=True)
    for j in range(len(menfo[i]) - 1):
        up, down = menfo[i][j], menfo[i][j+1]
        res.append([up - down - 1 - 1, -(up - 1)])
res.sort(reverse=True)
print(res)