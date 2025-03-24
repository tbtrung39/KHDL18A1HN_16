n = int(input("Nhập số tự nhiên n: "))
binary_str = ""
if n == 0:
    binary_str = "0"
else:
    while n > 0:
        binary_str = str(n % 2) + binary_str  # Lấy phần dư rồi ghép vào trước
        n //= 2  # Chia lấy phần nguyên

print("Số nhị phân:", binary_str)