def f(n):
    if n < 2:
        return n
    if n >= 2:
        return f(n%2) + f(n/2)

for i in range(2**100 + 1):
    if f(i) == 97:
        print(i)