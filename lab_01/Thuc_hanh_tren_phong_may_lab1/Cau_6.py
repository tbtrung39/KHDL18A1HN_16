# Các thông số cố định
hieu_dien_the = 220  # Vôn
cuong_do_dong_dien = 2.7  # Ampe
gia_dien = 7000  # đồng/kWh

# Nhập thời gian sử dụng bóng đèn (giây)
thoi_gian_su_dung = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))

# Tính công suất (W)
cong_suat = hieu_dien_the * cuong_do_dong_dien

# Đổi thời gian sử dụng từ giây sang giờ
thoi_gian_su_dung_gio = thoi_gian_su_dung / 3600

# Tính điện năng tiêu thụ (kWh)
dien_nang_tieu_thu = cong_suat * thoi_gian_su_dung_gio / 1000

# Tính tiền điện phải trả
so_tien = dien_nang_tieu_thu * gia_dien

# Làm tròn số tiền đến đơn vị đồng
so_tien = round(so_tien)

# In kết quả
print(f"Số tiền điện phải trả: {so_tien} đồng")