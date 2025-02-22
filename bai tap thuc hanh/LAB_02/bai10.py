gio_bat_dau = int(input("Nhập giờ bắt đầu (5-22): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc (5-22): "))
if 5 <= gio_bat_dau <= gio_ket_thuc <= 22:
    so_gio = gio_ket_thuc - gio_bat_dau
    gia_gio_dau = 100000
    gia_gio_sau = gia_gio_dau * 0.75
    if so_gio <= 3:
        tong_tien = so_gio * gia_gio_dau
    else:
        tong_tien = (3 * gia_gio_dau) + ((so_gio - 3) * gia_gio_sau)

    if 11 <= gio_bat_dau < 15 or 11 < gio_ket_thuc <= 15:
        tong_tien *= 0.9

    print("Số tiền phải trả là:", int(tong_tien),)