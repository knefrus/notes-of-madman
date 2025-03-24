def bn(tar, a):
    left, right = 0, len(a) - 1
    while left <= right:
        mid = (right + left) // 2
        if tar == a[mid]:
            return True
        elif tar < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False

f = open('files/279.txt')
n = f.readline()
#kolvo par, sr ar
#nechet, ar
pod = []
sp = sorted([int(x) for x in f])
for i in range(len(sp)):
    for j in range(i + 1, len(sp)):
        if (sp[i] % 2 != 0) and (sp[j] % 2 != 0) and bn(((sp[j] + sp[i]) // 2) , sp) == True:
            pod.append((sp[j] + sp[i]) // 2)

print(len(pod), max(pod))