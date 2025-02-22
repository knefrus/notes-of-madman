"""0 0 0 0
 в восьмиричной системе
 две одинаковых цифры рядом
"""

###----1----###

from itertools import product

def two(s):
    coup = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            coup += 1

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j] and abs(i - j) > 1:
                return 0

    return coup


k = 0
s = '01234567'

for a1, a2, a3, a4 in product(s, repeat=4):
    o = a1 + a2 + a3 + a4
    if a1 != '0':
        if two(o) == True:
            k += 1

print(k)"""


###----2----###

"""По факту достаточно посчитать с 11
Уможить на 7
И посчитать с 00 начиная со второй позиции
Типа 11xz * 7 + x00z * 8 + xz00 *8
О или даже так
В первом случае проверять чтобы x был отличным от пары ию
Во втором и икс и зед
В третьем только зед проверятт ??

























