f = open('files/269.txt')
n = f.readline()
ch = []
for i in f:
    st, en = map(int, i.split())
    ch.append([en, st])
ch.sort()

vt = []
goida = 0
for en, st in ch:
    if st >= goida:
        goida = en
        vt.append([st, en])
    if st >= 1386:
        print(en)
print(len(vt))