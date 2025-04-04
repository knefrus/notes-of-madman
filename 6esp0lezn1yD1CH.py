A = 76
fl = True
for x in range(1, 10000):
    for y in range(1, 10000):
        if ( ( (y + 3*x) < A) or ((2*y + x) > 50) or ((4*y - x) < 40) ) == False:
            fl = False
if fl == False:
    print(x,y)