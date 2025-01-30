def ZOV(k):
    a = [k-5]
    if k % 2 == 0:
        a.append(k // 2)
    if k % 3 == 0:
        a.append(k // 3)
    if k % 2 != 0 and k % 3 != 0:
        a.append(k + 1)
    return a

print([i for i in ZOV(5)])