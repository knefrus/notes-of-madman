f = open('files/24_2504.txt').readline().strip()
s = []
for i in range(len(f) - 4):
    if f[i] + f[i+1] + f[i+3] + f[i+4] == 'CBBC':
        s.append(f[i+2])

m = 0
c = ''

d = {x : s.count(x) for x in sorted(set(s))}
for x in d:
    if d[x] > m:
        m = d[x]
        c = x

print(c, m)