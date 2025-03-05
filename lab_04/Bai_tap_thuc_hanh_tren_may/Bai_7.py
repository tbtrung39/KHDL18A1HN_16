# Nhập hai số nguyên từ bàn phím
print("Nhập số nguyên thứ nhất:")
a = int(input())
print("Nhập số nguyên thứ hai:")
b = int(input())

# Đảm bảo hai số dương để tránh vòng lặp vô hạn
if a < 0:
    a = -a
if b < 0:
    b = -b

# Xác định số lớn hơn giữa a và b
if a > b:
    bcnn = a
else:
    bcnn = b

# Tìm BCNN bằng cách kiểm tra từng bội của số lớn hơn
while True:
    if bcnn % a == 0 and bcnn % b == 0:
        break  # Nếu chia hết cho cả a và b thì thoát vòng lặp
    bcnn += 1  # Tăng giá trị lên để kiểm tra tiếp

# In kết quả
print("Bội chung nhỏ nhất của", a, "và", b, "là:", bcnn)