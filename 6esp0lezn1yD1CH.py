def f(s, e):
    if s > e or s == 14:
        return 0
    if s == e:
        return 1
    return f(s + 2, e) + f(s * 2, e) + f(s * 3, e)
print(f(3, 12) * f(12, 46))