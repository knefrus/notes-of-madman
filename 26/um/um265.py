f = open('265.txt')
m = int(f.readline()) #zanyatih
places = [[m] * 100] #ЗАМЕНИТЬ НА 100001

for i in f:
    row, place = map(int, i.split())
    places[place].append(row)
print(places)