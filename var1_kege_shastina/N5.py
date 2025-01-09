sum = 0
min1 = 9999999
for i in range(0, 99999):
    N = bin(i)[2:]
    for k in N:
        sum = sum + int(k)
    if sum % 2 == 0:
        N = N + '11'
    else:
        N = N + '01'
    R = int(N, 2)
    sum = 0
    if R > 61:
        if R < min1:
            min1 = R

print(min1)