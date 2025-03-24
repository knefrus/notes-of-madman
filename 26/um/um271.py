f = open('files/271.txt')
n = f.readline()
boxes = [int(x) for x in f]
boxes.sort(reverse=True)

blocks = []
while boxes != []:
    goida = [boxes[0]]
    del boxes[0]
    for box in boxes[:]:
        if goida[-1] - box >= 5:
            goida.append(box)
            boxes.remove(box)
    blocks.append(goida)
print(len(blocks), len(blocks[0]))