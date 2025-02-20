U = 220  # Hiệu điện thế (V)
I = 2.7  # Cường độ dòng điện (A)
Gia_dien = 7000  # Giá điện (đ/kWh)

t = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))

P = U * I  # Công suất (W)
E = (P * t) / 3600  # Điện năng tiêu thụ (Wh)
Tien_dien = (E / 1000) * Gia_dien  # Quy đổi sang kWh và tính tiền

print("Tiền điện phải trả là:", round(Tien_dien, 2), "đ")
