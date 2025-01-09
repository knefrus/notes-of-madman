print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if (( (y <= x) and not(w) and z ) == 1):
                    print(w, x, y, z)