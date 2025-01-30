s = open('2.txt').readline().replace('-', '*').split('*')
dam = ''
dmax = ''

#132213**00**123*0123*0001234*0*123

for i in s:
    if len(i) != 0 and i[0] != '0':
        dam += i + '*'
    elif len(i) != 0 and i[0] == '0':
        dam += '0'
        dmax = max(dmax, dam, key=len)
        dam = str(int(i)) + '*'
    elif i == '0':
        dam += '0' + '*'
    else:
        dam = ''
    dmax = max(dmax, dam, key = len)
print(len(dmax) - 1)