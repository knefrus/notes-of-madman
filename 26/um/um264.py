import math as m

f = open('264.txt')
k = int(f.readline()) #kol-vo

poz = [int(i) for i in f] #vse
poz.sort()

b120 = [] #>120

for i in poz:
    if i > 120:
        b120.append(i)
b120.sort()

sum1 = 0
for i in range(len(b120) // 2):
    max = b120[i]
    sum1 += b120[i] * 0.25

print(m.ceil(sum(poz) - sum1))
print(max)