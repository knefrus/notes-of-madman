f = open('files/24_2506.txt').readline().strip()
d = { x : f.count(x) for x in sorted(set(f)) }

m = 0
c = ''
for x in d:
    if d[x] > m:
        m = d[x]
        c = x
print(c, m)