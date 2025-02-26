f = open('files/um263.txt')
n, m, k = map(int, f.readline().split())
#n - занято
#m - ряды
#k - места
mesta = [m] * (k + 1)
# ряд место
for i in f:
    ryad, mesto = map(int, i.split())
    mesta[mesto] = min(mesta[mesto], ryad - 1)

res = []
for i in range(1, len(mesta) - 1):
    left, right = mesta[i], mesta[i + 1]
    res.append([min(left, right), -i, -(i + 1)])
res.sort(reverse=True)
print(max(res))