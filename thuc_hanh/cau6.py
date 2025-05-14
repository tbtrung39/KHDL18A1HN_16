
def xu_ly_ma_tran():
    data = """4 211 133 180
192 168 1 254
11 1 11 233"""
    with open('matrix.txt', 'w') as file:
        file.write(data)
    with open('matrix.txt', 'r') as file:
        lines = file.readlines()
    print("Dòng 1:", lines[0].strip())
    print("Dòng 3:", lines[2].strip())
    print("\nToàn bộ file:")
    for line in lines:
        print(line.strip())
    odd_numbers = []
    for line in lines:
        numbers = list(map(int, line.strip().split()))
        odd_row = [num if num % 2 != 0 else 0 for num in numbers]
        odd_numbers.append(odd_row)
    while len(odd_numbers) < 4:
        odd_numbers.append([0]*4)
    for row in odd_numbers:
        while len(row) < 4:
            row.append(0)
    with open('ODD.txt', 'w') as file:
        for row in odd_numbers[:4]:  
            file.write(' '.join(map(str, row[:4])) + '\n')  
    with open('ODD.txt', 'r') as file:
        odd_lines = file.readlines()
    print("\nDòng cuối ODD.txt:", odd_lines[-1].strip())
xu_ly_ma_tran()
