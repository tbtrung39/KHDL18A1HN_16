with open(r"bai tap thuc hanh lab11\\bai2\\inp.txt", 'r') as file:
    line = file.readline()

numbers = list(map(int, line.split()))
numbers.sort()
with open('out.dat', 'w') as file:
    file.write(' '.join(map(str, numbers)))