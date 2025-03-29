import re
passwords = input("Nhập các mật khẩu (cách nhau bằng dấu phẩy): ").split(',')
valid_passwords = []
for password in passwords:
    password = password.strip()  
    if len(password) < 6 or len(password) > 12:
        continue
    if not re.search(r'[a-z]', password):  
        continue
    if not re.search(r'[0-9]', password):  
        continue
    if not re.search(r'[A-Z]', password):  
        continue
    if not re.search(r'[$#@]', password):  
        continue
    valid_passwords.append(password)
print(','.join(valid_passwords))
