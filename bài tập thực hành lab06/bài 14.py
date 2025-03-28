import re  
passwords = input("Nhập các mật khẩu (cách nhau bởi dấu phẩy): ").split(",")
valid_passwords = []
for password in passwords:
    password = password.strip()  
    if len(password) < 6 or len(password) > 12:
        continue  
    has_lower = any(c.islower() for c in password)  
    has_upper = any(c.isupper() for c in password)  
    has_digit = any(c.isdigit() for c in password)  
    has_special = any(c in "$#Q" for c in password)  
    if has_lower and has_upper and has_digit and has_special:
        valid_passwords.append(password)
print("Mật khẩu hợp lệ:", ", ".join(valid_passwords))