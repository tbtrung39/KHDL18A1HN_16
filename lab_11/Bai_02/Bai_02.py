
with open(r'lab_11\Bai_02\Inp.txt', 'r') as file:
    line = file.readline()

numbers = list(map(int, line.split()))
numbers.sort()
with open('out.dat', 'w') as file:
    file.write(' '.join(map(str, numbers)))