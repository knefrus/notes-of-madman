f = open('files/24_2500.txt').readline()
k = 0
for i in range(len(f) - 3):
    if f[i] + f[i+2] + f[i+3] == 'GME':
        k += 1
print(k)