# Nhập số nguyên từ người dùng
so = int(input("Nhập vào một số nguyên: "))

# Xử lý tìm chữ số hàng trăm
if so < 100 and so > -100:  # Nếu số có ít hơn 3 chữ số
    print(0)
elif so >= 100:  # Nếu số là số dương có từ 3 chữ số trở lên
    hang_tram = (so // 100) % 10
    print(hang_tram)
else:  # Nếu số là số âm có từ 3 chữ số trở lên
    hang_tram = abs(so) // 100 % 10
    print(hang_tram)