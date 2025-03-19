f = open('files/267.txt')
n = int(f.readline())
start = []
end = []
for i in range(n):
    sh, ok = map(int, f.readline().split())
    if ok < sh:
        end.append([ok, i + 1])
    else:
        start.append([sh, i + 1])
start.sort()
end.sort()
print(end)
print(max(start), max(end))
print(len(end) - 1)