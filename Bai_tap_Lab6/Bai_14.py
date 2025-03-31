import re
passwords = input("Nhập mật khẩu (cách nhau bằng dấu phẩy): ").split(',')
valid_passwords = []
for p in passwords:
    p = p.strip()
    if (re.search(r'[a-z]', p) and re.search(r'[0-9]', p) and 
        re.search(r'[A-Z]', p) and re.search(r'[$#@]', p) and 
        6 <= len(p) <= 12):
        valid_passwords.append(p)
print("Mật khẩu hợp lệ:", ", ".join(valid_passwords) if valid_passwords else "Không có mật khẩu hợp lệ")