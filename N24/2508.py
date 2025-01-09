m = 0
d = ''
for i in open('files/24_2508.txt'):
    if i.count('Q') >= m:
        m = i.count('Q')
        d = i.strip()        #строка нужная
m1 = 999999999999999999999
k = { x : d.count(x) for x in sorted(set(d)) }

c = ''
for x in k:
    if k[x] < m1:
        m1 = k[x]
        c = x
k1 = ''
for s in open('files/24_2508.txt'):
    k1+=s.strip()
print(k1.count('C'))