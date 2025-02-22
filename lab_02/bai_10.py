gio_bat_dau = int(input("Nhập giờ bắt đầu (5-22): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc (5-22): "))

if gio_bat_dau >= 5 and gio_ket_thuc <= 22 and gio_bat_dau < gio_ket_thuc:
    so_gio = gio_ket_thuc - gio_bat_dau
    tien = 0
    
    if so_gio == 1 or so_gio == 2 or so_gio == 3:
        tien = so_gio * 100000
    else:
        tien = 3 * 100000 + (so_gio - 3) * 75000

    if gio_bat_dau >= 11 and gio_ket_thuc <= 15:
        tien *= 0.9

    print("Số tiền cần trả:", int(tien), "VND")
else:
    print("Thời gian không hợp lệ!")