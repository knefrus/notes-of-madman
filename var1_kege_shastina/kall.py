from itertools import *
s1 = 'БЕНРСТЬЯ'
k1 = 0
k2 = 0
for x1, x2, x3, x4, x5 in permutations(s1, 5):
    s1 = x1 + x2 + x3 + x4 + x5
    k1 += 1
    if k1 % 2 == 0 and s1[:1] == 'Р':
        for i in s1:
            if i == 'Ь':
                k2 = 1
        if k2 == 0:
            print(k1, s1)
    k2 = 0
