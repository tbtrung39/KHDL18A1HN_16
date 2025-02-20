t = int(input("Nhập số giây sử dụng bóng đèn: "))

hieu_dien_the = 220  
cuong_do_dong_dien = 2.7  
gia_dien = 7000  

cong_suat = hieu_dien_the * cuong_do_dong_dien  
nang_luong_tieu_thu = (cong_suat * t) / (1000 * 3600)  
tien_dien = nang_luong_tieu_thu * gia_dien

print("Tiền điện phải trả là:", tien_dien, "đồng")