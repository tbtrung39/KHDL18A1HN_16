I = 2.7
U = 220
P = U * I
t = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))
E = (P * t) / 3600000  # Chuyển về kWh
tien_dien = E * 7000
print(f"Tiền điện phải trả: {tien_dien:.2f} đồng")