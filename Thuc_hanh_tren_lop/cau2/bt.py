with open('Inp.txt') as f:
    numbers = sorted(int(x) for x in f.read().split())

with open('out.dat', 'w') as f:
    f.write(' '.join(map(str, numbers)))
