f = open('files/24_2498.txt').readline().strip()
k = 0

for i in range(len(f) - 2):
    if f[i] + f[i+1] + f[i+2] == 'XIX':
        k+=1
print(k)