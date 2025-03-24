# Nhập chuỗi từ bàn phím
Str = input("Nhập chuỗi: ")

# Cách 1: Dùng công thức với thư viện re
import re
count1 = len(re.findall(r"[^a-zA-Z0-9]", Str))
print("Số ký tự không phải chữ cái và số (cách 1):", count1)

# Cách 2: Dùng vòng lặp
count2 = 0
for char in Str:
    if not ('a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9'):
        count2 += 1