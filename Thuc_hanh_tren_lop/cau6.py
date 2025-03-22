Str = input("Nhập chuỗi Str: ")
hex_chars = "0123456789ABCDEF"
result = ""
for char in Str:
    if char.upper() in hex_chars:
        result += char.upper()
if result == "":
    print("Chuỗi không hợp lệ.")
else:
    decimal_value = 0
    for char in result:
        decimal_value = decimal_value * 16 + "0123456789ABCDEF".index(char)
    print(f"Giá trị thập phân: {decimal_value}")
