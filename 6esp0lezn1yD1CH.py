f = open('text.txt').readline()
f = f.replace('*', '-')
f = f.split('-')
for i in f: