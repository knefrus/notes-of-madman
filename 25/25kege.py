from itertools import *
from fnmatch import *

def d(x):
    ds = {1, x}
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            ds |= {i, x // i}
        if len(ds) > 3:
            return [0]
    return sorted(ds)

# c=  0
# for i in range(1_125_000, 10 ** 10):
#     for a in d(i):
#         if a % 10 == 7 and a != 7 and a != i:
#             print(i, a)
#             c += 1
#             break
#     if c == 5:
#         break
#
# c = 0
# for i in range(310000, 10 ** 10):
#     ds = d(i)
#     #A
#     if len(ds) == 0:
#         A = 0
#     else:
#         A = int(sum(ds) / len(ds))
#     if A != 0 and A % 6 == 0 and A % 10 != 4:
#         c+=1
#         print(i, A)
#     if c == 6:
#         break
# for i in range(112_500_000, 112_550_000+1):
#     ds = d(i)
#     if len(ds) > 1:
#         M = sum(ds[-2:])
#     if M % 10000 == 1214:
#         print(i)
#
# for i in range(10**6, 10 ** 6):
#     ds = d(i)
#     d24 = [a for a in ds if str(a)[0] == '4']
#     if len(d24) == 24:
#         print(i, d24[-1])
# c = 0
# g = [2,3,5,7]
# for i in range(39345678, 0, -1):
#     ds = d(i)
#     Flag = True
#     if 76 <= len(ds) <= 88:
#         for a in g:
#             if a not in ds:
#                 Flag = False
#                 break
#         if Flag:
#             c += 1
#             print(i, len(ds))
#     if c == 10:
#         break
# c = 0
# for i in range(32_500_000, 10**10):
#     ds = d(i)
#     if len(ds) > 0 and sum(ds) % 145 == 0:
#         c += 1
#         print(i, sum(ds))
#     if c == 7:
#         break

from fnmatch import fnmatch

def divs(x):
  ds = set()
  for d in range(2, int(x**.5)+1):
    if x % d == 0:
      ds |= {d, x//d}
  return sorted(ds)

for sq in range(10**5):
  x = sq**2
  if fnmatch(str(x), '1?2*0*2?1'):
    if len(divs(sq)) == 0:
      print(x)