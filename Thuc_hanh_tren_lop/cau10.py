gio_bat_dau = int(input("Nhập giờ bắt đầu (5 <= giờ <= 22): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc (5 <= giờ <= 22): "))
if gio_bat_dau < 5 or gio_bat_dau > 22 or gio_ket_thuc < 5 or gio_ket_thuc > 22 or gio_bat_dau >= gio_ket_thuc:
    print("Giờ nhập không hợp lệ. Vui lòng nhập lại giờ bắt đầu và kết thúc.")
else:
    so_gio = gio_ket_thuc - gio_bat_dau
    tien = 0
    if so_gio <= 3:
        tien = so_gio * 100000  
    else:
        tien = 3 * 100000 + (so_gio - 3) * 100000 * 0.75  
    if 11 <= gio_bat_dau < 15 or 11 < gio_ket_thuc <= 15:
        tien = tien * 0.9  
    print(f"Số tiền khách thuê sân phải trả là: {tien:.0f} đồng")