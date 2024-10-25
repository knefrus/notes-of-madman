k = 0
for i in open('files/24_859.txt'):
    ik = i.strip()
    if ik.count('X') == ik.count('S'):
        k += 1
print(k)