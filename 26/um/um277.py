f = open('files/277.txt')
n = f.readline()
time = []
for s in f:
    st, en = map(int, s.split())
    time.append([en, st])

time.sort()
gg = 0
c = 0
gg2 = []
for en, st in time:
    if st > gg:
        gg = en
        gg2.append([st, en])
        c+=1
    if en <= 47:
        print(st)
print(c, gg2[0])