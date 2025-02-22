s = open('1.txt').readline()
s = s.replace('-', '*').split('*')

amd = ''
max1 = ''

# 123312**123*00123*00*123*0*123

for x in s:
    if len(x) != 0 and x[0] != '0':
        amd += x + '*'
    elif len(x) != 0 and x[0] == '0' and int(x) != 0:
        amd = str(int(x)) + '*'
    else:
        amd = ''
    max1 = max(max1, amd, key=len)

print(len(max1)-1)