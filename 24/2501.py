f = open('files/24_2501.txt').readline()
k = 0
for i in range(len(f) - 4):
    if f[i] + f[i+2] + f[i+4] == 'AAA':
        k += 1

print(k)