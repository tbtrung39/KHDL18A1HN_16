
str_input = input("Nhập một chuỗi bất kỳ: ")
valid_hex = ""
for char in str_input.upper():  
    if char in "0123456789ABCDEF":  
        valid_hex += char  
if valid_hex:
    decimal_value = int(valid_hex, 16) 
    print("Chuỗi hợp lệ sau khi loại bỏ:", valid_hex)
    print("Giá trị thập phân tương ứng là:", decimal_value)
else:
    print("Không có ký tự hợp lệ thuộc hệ Hex")