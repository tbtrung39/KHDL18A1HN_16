gio_bat_dau = int(input("Nhập giờ bắt đầu (5 <= giờ bắt đầu <= 22): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc (5 <= giờ kết thúc <= 22): "))

while gio_bat_dau < 5 or gio_bat_dau > 22 or gio_ket_thuc < 5 or gio_ket_thuc > 22 or gio_bat_dau >= gio_ket_thuc:
    gio_bat_dau = int(input("Nhập lại giờ bắt đầu (5 <= giờ bắt đầu <= 22): "))
    gio_ket_thuc = int(input("Nhập lại giờ kết thúc (5 <= giờ kết thúc <= 22): "))

so_gio_thue = gio_ket_thuc - gio_bat_dau
gia_gio_dau = 100000
gia_gio_sau = gia_gio_dau * 0.75
tien_thue = 0

if so_gio_thue <= 3:
    tien_thue = so_gio_thue * gia_gio_dau
else:
    tien_thue = 3 * gia_gio_dau + (so_gio_thue - 3) * gia_gio_sau

if 11 <= gio_bat_dau <= 15 or 11 <= gio_ket_thuc <= 15:
    tien_thue *= 0.9

print(f"Số tiền thuê sân bóng đá là: {tien_thue} đồng")