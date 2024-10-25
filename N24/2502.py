k = 0

for i in open('files/24_2502.txt'):
    ik = i.strip()
    for j in range(len(ik) - 3):
        if ik[j] + ik[j+2] + ik[j+3] == 'KGE':
            k+=1
            break

print(k)