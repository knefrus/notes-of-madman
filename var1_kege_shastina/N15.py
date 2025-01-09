for a in range (0, 100):
    c = 0
    for x in range(0, 101):
        for y in range(0, 101):
            if ( (x <= 19) or (y < (2 * x + a - 50)) or (y > 17)) == 1:
                c += 1
    if c == 100 * 100:
        print(a)
        break