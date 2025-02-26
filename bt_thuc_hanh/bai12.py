a_values = {
    'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19,
    'J': 20, 'K': 21, 'L': 23, 'M': 24, 'N': 25, 'O': 26, 'P': 27, 'Q': 28, 'R': 29,
    'S': 30, 'T': 31, 'U': 32, 'V': 34, 'W': 35, 'X': 36, 'Y': 37, 'Z': 38
}

code = input("Nhập mã container (9 ký tự, không bao gồm số kiểm tra): ").upper()

values = []
for i, char in enumerate(code):
    if char.isalpha():
        values.append(a_values[char])  
    else:
        values.append(int(char))  

max_ki = 0
for i, value in enumerate(values):
    max_ki += value * (2 ** i)

check = max_ki % 11

print(f"Số kiểm tra của mã container {code} là {check}")