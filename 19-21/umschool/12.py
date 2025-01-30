#19#

"""def ZOV(k, g, p):
    if (k + g) >= 89 and p == 2:
        return True
    if (k + g) >= 89 and p != 2:
        return False
    if (k + g) < 89 and p == 2:
        return False
    return ZOV(k + 2, g, p + 1) or ZOV(k, g * 3, p + 1) or ZOV(k * 3, g, p + 1) or ZOV(k, g + 2, p + 1)

for i in range(1, 79):
    if ZOV(10, i, 1):
        print(i)""" ##27##

#20#

"""def ZOV(k, g, p):
    if (k + g) >= 89 and p == 4:
        return True
    if (k + g) >= 89 and p != 4:
        return False
    if (k + g) < 89 and p == 4:
        return False
    if p % 2 == 0:
        return ZOV(k + 2, g, p + 1) and ZOV(k, g * 3, p + 1) and ZOV(k * 3, g, p + 1) and ZOV(k, g + 2, p + 1)
    if p % 2 != 0:
        return ZOV(k + 2, g, p + 1) or ZOV(k, g * 3, p + 1) or ZOV(k * 3, g, p + 1) or ZOV(k, g + 2, p + 1)

for i in range(1, 79):
    if ZOV(10, i, 1):
        print(i) """ ##2425##

#21#

def ZOV(k, g, p):
    if (k + g) >= 89 and ((p == 3) or (p == 5)):
        return True
    if (k + g) < 89 and p == 5:
        return False
    if (k + g) >= 89:
        return False
    if p % 2 == 1:
        return ZOV(k + 2, g, p + 1) and ZOV(k, g * 3, p + 1) and ZOV(k * 3, g, p + 1) and ZOV(k, g + 2, p + 1)
    else:
        return ZOV(k + 2, g, p + 1) or ZOV(k, g * 3, p + 1) or ZOV(k * 3, g, p + 1) or ZOV(k, g + 2, p + 1)

def VOZ(k, g, p):
    if (k + g) >= 89 and p == 3:
        return True
    if (k + g) >= 89 and p != 3:
        return False
    if (k + g) < 89 and p == 3:
        return False
    if p % 2 == 1:
        return VOZ(k + 2, g, p + 1) and VOZ(k, g * 3, p + 1) and VOZ(k * 3, g, p + 1) and VOZ(k, g + 2, p + 1)
    else:
        return VOZ(k + 2, g, p + 1) or VOZ(k, g * 3, p + 1) or VOZ(k * 3, g, p + 1) or VOZ(k, g + 2, p + 1)

for i in range(1, 79):
    if ZOV(10, i, 1) and not VOZ(10, i, 1):
        print(i)

#уничтожено :)