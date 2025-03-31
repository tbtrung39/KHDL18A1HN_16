import re
passwords = input("Nhập danh sách mật khẩu, phân tách bằng dấu phẩy: ").split(",")
valid_passwords = []
for password in passwords:
    password = password.strip()
    if 6 <= len(password) <= 12:
        if (re.search("[a-z]", password) and
            re.search("[0-9]", password) and
            re.search("[A-Z]", password) and
            re.search("[$#@]", password)):
            valid_passwords.append(password)

print(",".join(valid_passwords))