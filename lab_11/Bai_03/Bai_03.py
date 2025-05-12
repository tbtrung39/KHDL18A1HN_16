
with open(r'lab_11\Bai_03\f_in.dat', 'r') as file:
    line = file.readline()
    numbers = list(map(int, line.split()))
extremes = []
for i in range(1, len(numbers) - 1):
    if (numbers[i] > numbers[i-1] and numbers[i] > numbers[i+1]) or \
       (numbers[i] < numbers[i-1] and numbers[i] < numbers[i+1]):
        extremes.append(numbers[i])
with open('f_out.dat', 'w') as file:
    file.write(str(len(extremes)) + '\n')
    file.write(' '.join(map(str, extremes)))