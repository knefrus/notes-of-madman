from fnmatch import *
def f(x):
    mn = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            mn.add(i)
            mn.add(x // i)
    mn = sorted(list(mn))
    return mn

ans = 0

for i in range(960001, 10**10):
    sp = f(i)
    k = 0
    s = 0
    for j in sp:
        if len(f(j)) == 2 and fnmatch(str(j), '*3?'):
            k += 1
            s += j
    if k >= 3:
        ans += 1
        print(i, s)
    if ans == 5:
        break