f = open('92.txt')
k = 0
for s in f:
    st = sorted(map(int, s.split()))
    chet, nechet = [x for x in st if x % 2 == 0], [x for x in st if x % 2 != 0]
    if len(chet) % 2 == 0 and len(nechet) % 2 == 0:
        if len(nechet) > 0:
            if nechet[-1] % 3 == 0:
                k += 1
print(k)