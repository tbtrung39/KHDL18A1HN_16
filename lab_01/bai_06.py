hieu_dien_the = 220  
cuong_do_dong_dien = 2.7 
thoi_gian_giay = int(input("Nhap thoi gian su dung bong den (giay): "))
gia_tien_dien = 7000  
cong_suat = hieu_dien_the * cuong_do_dong_dien 
thoi_gian_gio = thoi_gian_giay / 3600 
dien_nang = cong_suat * thoi_gian_gio / 1000  
tong_tien = dien_nang * gia_tien_dien
print(f"Tien dien phai tra: {tong_tien:.2f} dong")