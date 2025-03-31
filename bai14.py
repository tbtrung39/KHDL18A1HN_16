import re

mat_khau = input("Nhập mật khẩu: ")

# Kiểm tra độ dài mật khẩu
if not (6 <= len(mat_khau) <= 12):
  print("Mật khẩu không hợp lệ: độ dài không hợp lệ")
else:
  # Kiểm tra các tiêu chí khác
  if not re.search("[a-z]", mat_khau):
    print("Mật khẩu không hợp lệ: thiếu chữ thường")
  elif not re.search("[0-9]", mat_khau):
    print("Mật khẩu không hợp lệ: thiếu số")
  elif not re.search("[A-Z]", mat_khau):
    print("Mật khẩu không hợp lệ: thiếu chữ hoa")
  elif not re.search("[$#@]", mat_khau):
    print("Mật khẩu không hợp lệ: thiếu ký tự đặc biệt")
  else:
    print("Mật khẩu hợp lệ")