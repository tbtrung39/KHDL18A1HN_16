char_map = {
    'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19, 'J': 20,
    'K': 21, 'L': 23, 'M': 24, 'N': 25, 'O': 26, 'P': 27, 'Q': 28, 'R': 29, 'S': 30, 'T': 31,
    'U': 32, 'V': 34, 'W': 35, 'X': 36, 'Y': 37, 'Z': 38
}
def calculate_check_digit(container_number):
    if len(container_number) != 10:
        return "Số container phải có 10 ký tự."
    total_weight = 0
    for i in range(10):
        char = container_number[i]
        if char.isalpha(): 
            value = char_map[char]
        else:  
            value = int(char)
        total_weight += value * (2 ** i)
    check_digit = total_weight % 11
    return check_digit
container_number = input("Nhập số container (10 ký tự): ")
check_digit = calculate_check_digit(container_number)
print(f"Số kiểm tra của container {container_number} là: {check_digit}")
