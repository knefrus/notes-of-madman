f = open('files/268.txt')
n = f.readline()

sec = [0] * 86400
izm = [0] * 86400

for t in f:
    s, e = map(int, t.split())
    izm[s] += 1
    izm[e] -= 1
cnt = 0
for t in range(86400):
    cnt += izm[t]
    sec[t] = cnt
print(max(sec[8 * 60 * 60 : 14 * 60 * 60 + 1]))
print(sec.count(max(sec[8 * 60 * 60 : 14 * 60 * 60 + 1])))