#19:
"""def g(k, pos, end):
    if k >= 56 and pos == end:
        return True
    if k >= 56 and pos != end:
        return False
    if k < 56 and pos == end:
        return False
    if (pos + 1) % 2 == (end % 2):
        return g(k + 1, pos + 1, end) or g(k * 3, pos + 1, end)
    else:
        return g(k + 1, pos + 1, end) or g(k * 3, pos + 1, end)

for i in range(1, 56):
    if g(i, 0, 2):
        print(i)

"""

#20:

"""def g(k, pos, end):
    if k >= 56 and pos == end:
        return True
    if k >= 56 and pos != end:
        return False
    if k < 56 and pos == end:
        return False
    if (pos + 1) % 2 == (end % 2):
        return g(k + 1, pos + 1, end) or g(k * 3, pos + 1, end)
    else:
        return g(k + 1, pos + 1, end) and g(k * 3, pos + 1, end)

for i in range(1, 56):
    if g(i, 0, 3):
        print(i)"""

#21:

def g(k, pos, end):
    if k >= 56 and pos in end:
        return True
    if k >= 56 and pos not in end:
        return False
    if k < 56 and pos == max(end):
        return False
    if (pos + 1) % 2 == (end[0] % 2):
        return g(k + 1, pos + 1, end) or g(k * 3, pos + 1, end)
    else:
        return g(k + 1, pos + 1, end) and g(k * 3, pos + 1, end)

for i in range(1, 56):
    if g(i, 0, [2, 4]) and not g(i, 0, [2]):
        print(i)

#уничтожено :)