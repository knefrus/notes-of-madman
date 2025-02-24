f = open('um261.txt')
n, m, k = map(int, f.readline().split())
# n занятых
# m рядов
# k мест

minfo = [m] * (k+1)

for i in f:
    ryad, mesto = map(int, i.split())
    minfo[mesto] = min(minfo[mesto], ryad - 1)

res = []
for i in range(1, len(minfo) - 1):
    left, right = minfo[i], minfo[i+1]
    res.append([min(right, left), i, i+1])
print(max(res))