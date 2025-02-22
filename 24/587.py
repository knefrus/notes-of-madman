k = 0
for i in open('files/24_587.txt'):
    ik = i.strip()
    B1 = ik.count('B')
    A1 = ik.count('A')
    if (B1 - A1)/A1 * 100 >= 5:
        k+=1
print(k)