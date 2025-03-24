# Nhập chuỗi từ bàn phím
Str = input("Nhập chuỗi: ")

# Cách 1: Dùng công thức với re
import re
hex_str1 = re.sub(r"[^0-9A-Fa-f]", "", Str)  # Loại bỏ ký tự không thuộc hệ Hex
if hex_str1:  # Nếu còn chuỗi hợp lệ
    decimal_value1 = int(hex_str1, 16)
    print("Chuỗi hợp lệ sau khi lọc (cách 1):", hex_str1)
    print("Giá trị thập phân (cách 1):", decimal_value1)
else:
    print("Không có ký tự hợp lệ trong chuỗi!")

# Cách 2: Dùng vòng lặp
hex_str2 = ""
for char in Str:
    if ('0' <= char <= '9') or ('A' <= char <= 'F') or ('a' <= char <= 'f'):
        hex_str2 += char

if hex_str2:  # Nếu còn chuỗi hợp lệ
    decimal_value2 = 0
    base = 1  # Hệ số của từng chữ số theo hệ Hex

    for i in range(len(hex_str2) - 1, -1, -1):  # Duyệt từ cuối về đầu
        if '0' <= hex_str2[i] <= '9':
            value = ord(hex_str2[i]) - ord('0')  # Chuyển số
        else:
            value = ord(hex_str2[i].upper()) - ord('A') + 10  # Chuyển chữ cái A-F

        decimal_value2 += value * base
        base *= 16  # Nhân với 16 để lên hàng tiếp theo

    print("Chuỗi hợp lệ sau khi lọc (cách 2):", hex_str2)
    print("Giá trị thập phân (cách 2):", decimal_value2)
else:
    print("Không có ký tự hợp lệ trong chuỗi!")