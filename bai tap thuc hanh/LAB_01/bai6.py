t = float(input("Thời gian sử dụng bóng đèn (s): "))
E_kWh = (220 * 2.7 * t) / 3600000  
tien_dien = E_kWh * 7000
print(f"Số tiền điện phải trả: {tien_dien:.2f} VNĐ")