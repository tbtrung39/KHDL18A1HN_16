import re

# Nhập danh sách mật khẩu từ người dùng (các mật khẩu phân tách bởi dấu phẩy)
passwords = input("Nhập các mật khẩu, cách nhau bởi dấu phẩy: ").split(",")

# Danh sách để lưu mật khẩu hợp lệ
valid_passwords = []

# Kiểm tra từng mật khẩu trong danh sách
for password in passwords:
    password = password.strip()  # Loại bỏ khoảng trắng hai đầu
    
    if (6 <= len(password) <= 12 and 
        re.search(r"[a-z]", password) and  # Ít nhất 1 chữ thường
        re.search(r"[0-9]", password) and  # Ít nhất 1 chữ số
        re.search(r"[A-Z]", password) and  # Ít nhất 1 chữ hoa
        re.search(r"[$#@]", password)):    # Ít nhất 1 ký tự đặc biệt
        
        valid_passwords.append(password)

# In kết quả, các mật khẩu hợp lệ được nối lại bằng dấu phẩy
print(",".join(valid_passwords))