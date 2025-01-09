sp1 = [0] * 3215
sp2 = [0] * 3215

for n in range(3214, 10, -1):
    if n >= 3210:
        sp1[n] = 1
    elif n < 3210:
        sp1[n] = sp1[n+3] + 7

for k in range(7, 3100):
    if k < 10:
        sp2[k] = k
    elif k >= 10:
        sp2[k] = sp2[k-3] + 5

print(sp1[15] - sp2[3000])