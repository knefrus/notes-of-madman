f = open('91.txt')

k = 0

for s in f:
    t = sorted(map(int, s.split()))
    if (t[0] + t[1]) == (t[2] + t[3]) or (t[0] + t[2]) == (t[1] + t[3]) or (t[0] + t[3]) == (t[1] + t[2]):
        if t[-1] - t[0] > ((t[1] + t[2]) - t[-1]):
            k += 1
print(k)