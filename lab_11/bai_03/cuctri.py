
with open(r"bai_03\f_in.dat", 'r') as file:
    line = file.readline()

numbers = list(map(int, line.split()))
numbers.sort()
with open('f_out.dat', 'w') as file:
    file.write(' '.join(map(str, numbers)))