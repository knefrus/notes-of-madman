f = open('files/24_2505.txt').readline().strip()
s = []
for i in range(len(f) - 2):
    if f[i] == f[i+2]:
        s.append(f[i+1])

d = { x : s.count(x) for x in sorted(set(s)) }

m = 0
c = ''
for x in d:
    if d[x] > m:
        m = d[x]
        c = x

print(c, m)