f = open('files/24_2509.txt').readline().strip()
d = { x : f.count(x) for x in sorted(set(f)) }

m = 0
mn = 10**10

for x in d:
    if d[x] > m:
        m = d[x]
    if d[x] < mn:
        mn = d[x]

print(m-mn)