f = open('files/273.txt')
n = f.readline()
tort = [int(x) for x in f]
tort.sort(reverse=True)
goida = [tort[0]]
for s in tort:
    if goida[-1] - s >= 7:
        goida.append(s)
print(len(goida), goida[-1])