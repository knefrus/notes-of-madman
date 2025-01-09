sp = [0] * 13800

for i in range(1, 13767):
    if i < 5:
        sp[i] = i
    else:
        sp[i] = 2* i * sp[i-4]
print(  (sp[13766] - 9 * sp[13762]) / sp[13758] )