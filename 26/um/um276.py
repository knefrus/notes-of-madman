f = open('files/276.txt')
n = int(f.readline())
shs = []
oks = []
for i in range(n):
    sh, ok = map(int, f.readline().split())
    if sh < ok:
        shs.append([sh, i + 1])
    else:
        oks.append([ok, i + 1])

print(max(shs), max(oks))
print(len(shs) - 1)