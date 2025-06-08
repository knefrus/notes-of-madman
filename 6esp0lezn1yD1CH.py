
# from itertools import *
# c = 0
# for i in permutations("КАЛИЙ", r = 5):
#     a = "".join(i)
#     if a[0] != "Й" and "ИА" not in a:
#         c += 1
# print(c)

# from itertools import *
# c = 0
# for i in permutations("АМФИБРАХИЙ"):
#     a = "".join(i)
#     if "ИИФАА" in a or "ААФИИ" in a:
#         c+=1
# print(c)

from itertools import *
# c = 0
# for i in set(product("0123456", repeat=7)):
#     a = "".join(i)
#     if a[0] not in "035" and ('22' not in a or '44'not in a):
#         c += 1
#
# print(c)

# a = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'[::-1]
# b = [a.index(x) for x in "ИНФОРМАТИКА"]
# s = 1
# for i in range(len(b)):
#     s += b[i] * 33 ** (len(b)- i - 1)
# print(s)
#
# from itertools import *
#
# k = 0
# for i in product('01234', repeat = 6):
#     a = ''.join(i)
#     if a[0] == '3' and int(a, 5) % 2 == 0:www
#         k+= 1
# print(k)
#
# print(len(set(str(hex(4 ** 36 + 3 * 4 ** 20 + 4 ** 15 + 2 * 4 ** 7 + 49)[2:]))))
#
# def f(k):
#     j = 0
#     while k > 0:
#         j += k % 4
#         k //= 4
#     return j
# res = set()
# for x in range(0, 10000000):
#     a = 3*16**2018 - 2*8**1028 - 3*4**1100 - 4**x - 2022
#     if a <= 0:
#         break
#     h = f(a)
#     res.add(h)
# print(len(res))
# for i in range(2, 100):
#     a = 70
#     k = 0
#     while a > 0:
#         a = a // i
#         k += 1
#     if k == 3:
#         print(i)
#         break
#
# for N in range(1, 1000):
#     if 41 % N == 2 and 131 % N == 1:
#         print(N)
#         break
# k = 0
# for N in range(1, 10000):
#     if 39 % N == 3:
#         k += 1
#
# print(k)
# for x in range(0, 32):
#     if int('33', x + 4) - int('33', 4) == 33:
#         print(x)
# def fs(k, x):
#     s = ''
#     while x > 0:
#         s+=str(x%k)
#         x //= k
#     return s[::-1]
#
# def fs2(k, p):
#     x = str(p)[::-1]
#     r = 0
#     for j in range(0, len(x)):
#         r += int(x[j]) * k**j
#     return r
#
#
# a = 43*7**103 - 21*7**57 + 98
# a = fs(7, a)
# print(sum([int(x) for x in a]))

# for x in range(0, 1000):
#     a = 36**17 - 6**x + 71
#     s = 0
#     while a > 0:
#         s += a % 6
#         a //= 6
#     if s == 61:
#         print(x)
#         break
#
# for x in range(2030, 0, -1):
#     a = 3**100 - x
#     a1 = a
#     k = 0
#     while a > 0:
#         if a % 3 == 0:
#             k+= 1
#         a //= 3
#     if k == 1:
#         print(a1, x)
#         break
#
# for x in '0123456789ABCDEFGHIJK':
#     a = int(f'82934{x}2', 21) + int(f'2924{x}{x}7',21) + int(f'67564{x}8',21)
#     if a % 20 == 0:
#         print(a // 20)
#         break
#
# for x in '0123456789ABCDE':
#     a = int(f'1{x}51', 15) - int(f'3{x}2', 15)
#     if a % 4 == 0:
#         print(a // 4)
#
# for x in '0123456789ABCDE':
#     for y in '0123456789ABCDEFG':
#         a = int(f'123{x}5', 15) + int(f'67{y}9', 17)
#         if a % 131 == 0:
#             print(a // 131, y)
# for x in range(0, 111):
#     a1 = 0
#     a2 = 0
#     a1 = x*111**3+3*111**2+2*111+1
#     a2 = 1*211**3+7*211**2+x*211+4
#     a = a1 + a2
#     if a % 111 == 0:
#         print(a // 111)

for x in range(0, 37):
    a = 13*37**8 + 5*37**7 + 9*37**6 + x*37**5 + 12*37**4 + 11*37**3 + 9 *37**2 + 8*37**1 + 16*37**0
    a2 = 15*37**8 + 3*37**7 + x*37**6 + 5*37**5 + 14*37**4 + 11*37**3 + 9*37**2 + 13*37**1 + 6*37**0
    if (a * a2) % 36 == 0 :
        print(2*37**2 + x*37**1+1*37**0)