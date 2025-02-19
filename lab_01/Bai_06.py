
U = 220  
I = 2.7  
gia_dien = 7000  
thoi_gian = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))
P = U * I
nang_luong_tieu_thu = (P * thoi_gian) / (1000 * 3600)
tien_dien = nang_luong_tieu_thu * gia_dien
tien_dien = round(tien_dien, 2)
print("Số tiền điện phải trả là:", tien_dien,"đồng")