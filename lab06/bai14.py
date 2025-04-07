# Nhập mật khẩu từ người dùng
password = input("Nhập mật khẩu của bạn: ")

# Kiểm tra độ dài mật khẩu
if len(password) < 6 or len(password) > 12:
    print("Mật khẩu phải có độ dài từ 6 đến 12 ký tự.")
else:
    # Kiểm tra có ít nhất 1 chữ cái viết thường [a-z]
    has_lower = False
    # Kiểm tra có ít nhất 1 chữ cái viết hoa [A-Z]
    has_upper = False
    # Kiểm tra có ít nhất 1 số [0-9]
    has_digit = False
    # Kiểm tra có ít nhất 1 ký tự đặc biệt [$ # @]
    has_special = False
    
    for char in password:
        if 'a' <= char <= 'z':
            has_lower = True
        elif 'A' <= char <= 'Z':
            has_upper = True
        elif '0' <= char <= '9':
            has_digit = True
        elif char in ['$', '#', '@']:
            has_special = True
    
    # Kiểm tra tất cả các điều kiện
    if has_lower and has_upper and has_digit and has_special:
        print("Mật khẩu hợp lệ!")
    else:
        if not has_lower:
            print("Mật khẩu phải chứa ít nhất 1 chữ cái viết thường (a-z).")
        if not has_upper:
            print("Mật khẩu phải chứa ít nhất 1 chữ cái viết hoa (A-Z).")
        if not has_digit:
            print("Mật khẩu phải chứa ít nhất 1 số (0-9).")
        if not has_special:
            print("Mật khẩu phải chứa ít nhất 1 ký tự đặc biệt ($, #, @).")