# Nhập bán kính và chiều cao từ bàn phím
r = float(input("Nhập bán kính (r): "))
h = float(input("Nhập chiều cao (h): "))

# Định nghĩa giá trị của pi
pi = 3.14

# Tính diện tích xung quanh
dien_tich_xung_quanh = 2 * pi * r * h

# Tính diện tích toàn phần
dien_tich_toan_phan = 2 * pi * r * (r + h)

# Tính thể tích khối trụ
the_tich = pi * r**2 * h

# In ra kết quả, làm tròn đến 2 chữ số thập phân
print(f"Diện tích xung quanh: {round(dien_tich_xung_quanh, 2)}")
print(f"Diện tích toàn phần: {round(dien_tich_toan_phan, 2)}")
print(f"Thể tích khối trụ: {round(the_tich, 2)}")