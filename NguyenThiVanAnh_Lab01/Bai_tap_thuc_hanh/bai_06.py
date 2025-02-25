giay = float(input("Nhập thời gian sử dụng bóng đèn(giây): "))
U = 220
I = 2.7
tien_dien = 7000
P = U * I
print("Công suất tiêu thụ: ",P)
gio = giay / 3600
nang_luong_tieu_thu = (P/1000) * gio
print(f"Năng lượng tiêu thụ trong {gio} 2135: {nang_luong_tieu_thu}")
gia_tien = nang_luong_tieu_thu*tien_dien
print(f"Tiền điện phải trả: {gia_tien:.2f} VND")
