# Bảng mã hóa ký tự chữ cái theo giá trị tương ứng
char_map = {
    'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19, 
    'J': 20, 'K': 21, 'L': 23, 'M': 24, 'N': 25, 'O': 26, 'P': 27, 'Q': 28, 'R': 29, 
    'S': 30, 'T': 31, 'U': 32, 'V': 34, 'W': 35, 'X': 36, 'Y': 37, 'Z': 38
}
container = input("Nhập số container (10 ký tự): ")

# Kiểm tra độ dài hợp lệ
while len(container) != 10:
    container = input("Nhập lại số container hợp lệ (10 ký tự): ")

# Mã hóa 4 ký tự đầu
encoded = []
i = 0
while i < 4:
    encoded.append(char_map[container[i]])
    i += 1

# Thêm 6 ký tự số còn lại
i = 4
while i < 10:
    encoded.append(int(container[i]))
    i += 1
total = 0
i = 0
while i < 10:
    total += encoded[i] * (2 ** i)
    i += 1

check_digit = total % 11
if check_digit == 10:
    check_digit = 0  # Theo chuẩn, nếu dư 10 thì đổi thành 0

print("Số kiểm tra (Check Digit):", check_digit)
