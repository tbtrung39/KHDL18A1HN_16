
gio_bat_dau = int(input("Nhập giờ bắt đầu (≥ 5 giờ): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc (≤ 22 giờ): "))
so_gio_thue = gio_ket_thuc - gio_bat_dau
if gio_bat_dau < 5 or gio_ket_thuc > 22 or so_gio_thue <= 0:
    print("Giờ nhập không hợp lệ.")
else:
    if so_gio_thue <= 3:
        tien = so_gio_thue * 100000
    else:
        tien = 3 * 100000 + (so_gio_thue - 3) * 100000 * 0.75  
    if gio_bat_dau >= 11 and gio_ket_thuc <= 15:
        tien *= 0.9  
    print("Số tiền khách phải trả là:", tien, "đồng")