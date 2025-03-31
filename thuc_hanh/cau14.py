import re

passwords = input("Nhập danh sách mật khẩu (cách nhau bằng dấu phẩy): ").split(',')
valid_passwords = []

for password in passwords:
    if len(password) < 6 or len(password) > 12:
        continue
    if not re.search("[a-z]", password):  # Ít nhất 1 chữ cái thường
        continue
    if not re.search("[0-9]", password):  # Ít nhất 1 số
        continue
    if not re.search("[A-Z]", password):  # Ít nhất 1 chữ cái hoa
        continue
    if not re.search("[$#@]", password):  # Ít nhất 1 ký tự đặc biệt ($, #, @)
        continue
    
    valid_passwords.append(password)

print("Mật khẩu hợp lệ:", ", ".join(valid_passwords))
