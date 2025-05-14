# Câu 3
# Cách 1:
n = int(input("Nhập một số tự nhiên: "))
binary = bin(n)[2:]  # Dùng hàm bin() và bỏ ký tự '0b'
print("Số", n, "trong hệ nhị phân là:", binary)
# Cách 2:
n = int(input("Nhập một số nguyên: "))
binary = ""
if n == 0:
    binary = "0"
else:
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
print("Số nhị phân tương ứng là:", binary)