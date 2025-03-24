f = open('files/270.txt')
n = f.readline()

boxes = [int(x) for x in f]
boxes.sort(reverse=True)

goida = [boxes[0]]
for box in boxes:
    if goida[-1] - box >= 5:
        goida.append(box)
print(goida)