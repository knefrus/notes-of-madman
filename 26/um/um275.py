f = open('files/275.txt')
n = f.readline()

sp = []

for s in f:
    st, en = map(int, s.split())
    sp.append([en, st])
sp.sort()

mer = 0
pod = []
maxi = []
for en, st in sp:
    if st >= mer:
        mer = en
        pod.append([st, en])
    if st >= 1359:
        maxi.append(en)
print(len(pod), maxi[-1])