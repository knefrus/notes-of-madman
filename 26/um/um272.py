f = open('files/272.txt')
n = f.readline()
boxes = []
for i in f:
    st, col = i.split()
    st = int(st)
    boxes.append([st, col])

pack = []
boxes.sort(reverse=True)
while boxes != []:
    goida = [boxes[0]]
    del(boxes[0])
    for box in boxes[:]:
        if goida[-1][0] - box[0] >= 8 and goida[-1][1] != box[1]:
            goida.append(box)
            boxes.remove(box)
    pack.append(goida)

print(len(pack[0]), len(pack))

