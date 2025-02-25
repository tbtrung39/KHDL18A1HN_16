# Nhập các thông số đầu vào
U = 220  # hiệu điện thế (V)
I = 2.7  # cường độ dòng điện (A)
gia_tien_dien = 7000  # giá tiền điện (đ/kWh)

# Nhập thời gian sử dụng bóng đèn (giây)
t = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))

# Tính công suất tiêu thụ
P = U * I  # Công suất tiêu thụ (W)

# Tính năng lượng tiêu thụ trong kWh
nang_luong_tieu_thu_kWh = (P * t) / 3600000  # 1 kWh = 1000 W * 3600 s

# Tính tiền điện
tien_dien = nang_luong_tieu_thu_kWh * gia_tien_dien

# Hiển thị kết quả
print(f"Tiền điện phải trả: {tien_dien:.2f} đ")
