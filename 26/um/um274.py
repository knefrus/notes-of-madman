f = open('files/274.txt')
n, k = map(int, f.readline().split())
#k - Дисков
files = []
d = [0] * k #диски
for s in f:
    st, en = map(int, s.split())
    files.append([st, en])
files.sort()
j = 0 #счетчик общий
j2 = 0 #счетчик последнего
for st, en in files:
    for i in range(k):
        if st >= d[i]:
            d[i] = en + 1
            j += 1
            j2 = i + 1
            break
print(j, j2)