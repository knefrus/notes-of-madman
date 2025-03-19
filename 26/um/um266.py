f = open('files/266.txt')
n, k = map(int, f.readline().split())
#n - файлов
#k - дисков

files = []

for i in f:
    start, end = map(int, i.split())
    files.append([start, end])
files.sort()
c = 0
last = 0
disk = [0] * k

for start, end in files:
    for i in range(k):
        if start > disk[i]:
            disk[i] = end
            c += 1
            last = i + 1
            break
print(c, last)