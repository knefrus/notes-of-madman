def bin(target, a):
    left, right = 0, len(a) - 1
    while left <= right:
        mid = (right + left) // 2
        if a[mid] == target:
            return True
        elif a[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

f = open('files/278.txt')
n = f.readline()
sp = sorted([int(x) for x in f])
sp2 = []
for i in range(len(sp)):
    for j in range(i + 1, len(sp)):
        if ((sp[i] % 2) != (sp[j] % 2)) and (bin(sp[i] + sp[j], sp) == True):
            sp2.append(sp[i] + sp[j])
print(len(sp2), max(sp2))