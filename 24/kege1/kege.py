# s = open('24_1_1.txt').readline()
#
# while 'XXXXX' in s:
#     s = s.replace('XXXXX', 'XXXX XXXX')
# print(s.count('XXXX'))
#
# s = open('24_2_1.txt').readline()
# s = s.replace('G', ' ').replace('W', ' ').replace('P', ' ')
# print(max([len(k) for k in s.split()]))
#
# s = open('24_3_1.txt').readline()
# s = s.replace('XZZY', 'XZZ ZZY')
# print(max([len(k) for k in s.split()]))
#
# s = open('24_4_1.txt').readline()
# s = s.replace('XX', ' ').replace('YY', ' ').replace('ZZ', ' ')
# print(max([len(k) for k in s.split()]))
#
# s = open('24_5_1.txt').readline()
#
# for x in range(10):
#     for y in range(10):
#         if x + y < 10:
#             while str(x) + str(y) in s:
#                 s = s.replace(str(x)+str(y), str(x)+ ' ' +str(y))
#
# print(max([len(k) for k in s.split()]))
#
# s = open('24_6_1.txt').readline()
# s = s.replace('4', '2').replace('3', '1').replace('5', '1')
# while '11' in s:
#     s = s.replace('11', '1 1')
# while '22' in s:
#     s = s.replace('22', '2 2')
# s = s.replace('12', '*')
# s = s.replace('1', ' ').replace('2',' ')
# print(max([len(k) for k in s.split()]))
#
# s = open('24_7_1.txt').readline()
#
from re import finditer
# pat = r'(?=((D[^OD]*(O[^OD]*){,2})+D))'
# mx = 0
# for m in finditer(pat, s):
#     mx = max(mx, len(m[1]))
# print(mx)
#
# s = open('24_8_1.txt').readline()
# hui = r"((AC|AB)+)"
# mx = 0
# for m in finditer(hui, s):
#     mx = max(mx, len(m[1]))
#     print(m.group())
# print(mx)
#
# s = open('24_3584.txt').readline()
# pat = r'(BA|DA)+'
# print(max(len(m[0]) for m in finditer(pat, s))//2)
#
# s = open('24_11_1.txt').readline()
# pat = r"(?=([^.]*(.[^.]*){,5}))"
# print(max(len(m[1]) for m in finditer(pat, s)))
#
# s = open('24_12_1.txt').readline()
# pat = '(?=((XYZ|XY|YZ)+))'
# print(max(len(m[1]) for m in finditer(pat, s)))
#
# s = open('24_13_1.txt').readline()
# pat = '(LMN|MN|N)?(KLMN)+(KLM|KL|K)?'
# print(max(len(m[0]) for m in finditer(pat, s)))
#
# s = open('24_14_1.txt').readline()
# pat = '(?=([^AR]*(A[^AR]*){,3}))'
# mx = 0
# for x in finditer(pat, s):
#     mx = max(mx, len(x[1]))
# print(mx)
#0123456789AB
# s = open('24_15_1.txt').readline()
# pat = r'(?=([123456789AB][0123456789AB]*[02468A]))'
# mx = 0
# for x in finditer(pat, s):
#     mx = max(mx, len(x[1]))
# print(mx)
#
# s = open('24_16_1.txt').readline()
# ch = '([789][0789]*)'
# pat = fr'({ch}[*-])*{ch}'
# mx = 0
# for x in finditer(pat, s):
#     mx = max(len(x[0]), mx)
# print(mx)
#
def F(s, p, e):
    if s >= 54 and p in e:
        return 1
    elif s >= 54 and p not in e:
        return 0
    elif s < 54 and p == max(e):
        return 0
    if p % 2 == max(e) % 2:
        return F(s + 2, p + 1, e) and F(s * 2, p + 1, e)
    return F(s + 2, p + 1, e) or F(s * 2, p + 1, e)



for s in range(1, 53):
    if F(s, 0, [2,4]) and not F(s, 0, [2]):
        print(s)