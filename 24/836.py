f = open('files/24_836.txt').readline()
k = 0
for i in range(len(f) - 4):
    if f[i] + f[i+1] + f[i+2] + f[i+3] + f[i+4] == f[i+4] + f[i+3] + f[i+2] + f[i+1] + f[i]:
        k+=1

print(k)