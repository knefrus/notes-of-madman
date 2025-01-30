#20#
"""
def g(k, s, p):

    if (s + k) >= 80 and p == 4: return True
    if (s + k) >= 80: return False
    if (s + k) < 80 and p == 4: return False
    if p % 2 == 1:
        return g(k + 1, s, p + 1) or g(k * 3, s, p + 1) or g(k, s + 1, p + 1) or g(k, s * 3, p + 1)
    else:
        return g(k + 1, s, p + 1) and g(k * 3, s, p + 1) and g(k, s + 1, p + 1) and g(k, s * 3, p + 1)

for i in range(1, 77):
    if g(3, i, 1):
        print(i)
"""

#21#
def g(k, s, p):

    if (s + k) >= 80 and ((p == 3) or (p == 5)): return True
    if (s + k) >= 80: return False
    if (s + k) < 80 and p == 5: return False
    if p % 2 == 0:
        return g(k + 1, s, p + 1) or g(k * 3, s, p + 1) or g(k, s + 1, p + 1) or g(k, s * 3, p + 1)
    else:
        return g(k + 1, s, p + 1) and g(k * 3, s, p + 1) and g(k, s + 1, p + 1) and g(k, s * 3, p + 1)

def ga(k, s, p):

    if (s + k) >= 80 and p == 3: return True
    if (s + k) >= 80: return False
    if (s + k) < 80 and p == 3: return False
    if p % 2 == 0:
        return ga(k + 1, s, p + 1) or ga(k * 3, s, p + 1) or ga(k, s + 1, p + 1) or ga(k, s * 3, p + 1)
    else:
        return ga(k + 1, s, p + 1) and ga(k * 3, s, p + 1) and ga(k, s + 1, p + 1) and ga(k, s * 3, p + 1)

for i in range(1, 77):
    if g(3, i, 1) and not ga(3, i, 1):
        print(i)