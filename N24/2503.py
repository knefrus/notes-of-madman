k = 0

for i in open('files/24_2503.txt'):
    ik = i.strip()
    O1 = 0
    A1 = 0
    for l in range(len(ik) - 2):
        if ik[l] + ik[l+1] + ik[l+2] == 'OAO':
            O1+=1
        if ik[l] + ik[l + 1] + ik[l + 2] == 'AOA':
            A1 += 1
    if A1 > O1:
        k+=1
print(k)