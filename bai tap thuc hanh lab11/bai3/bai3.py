with open(r"bai tap thuc hanh lab11\\bai3\\f_in.dat", 'r') as file:
    line = file.readline()

numbers = list(map(int, line.split()))
numbers.sort()
with open('bai tap thuc hanh lab11\\bai3\\f_out.dat', 'w') as file:
    file.write(' '.join(map(str, numbers)))