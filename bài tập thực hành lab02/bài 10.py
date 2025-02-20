gio_bat_dau = int(input("Nhập vào giờ bắt đầu (5-22): "))
gio_ket_thuc = int(input("Nhập vào giờ kết thúc (5-22): "))
if 5 <= gio_bat_dau <= gio_ket_thuc <= 22:
    tong_gio_thue = gio_ket_thuc - gio_bat_dau
    if tong_gio_thue <= 3:
        tien_thue = tong_gio_thue * 100000
    else:
        tien_thue = 3 * 100000 + (tong_gio_thue - 3) * (100000 * 0.75)
    if gio_bat_dau <= 15 <= gio_ket_thuc or gio_bat_dau <= 11 <= gio_ket_thuc or (11 <= gio_bat_dau and gio_ket_thuc <= 15):
        tien_thue *= 0.90
    print(f"Số tiền khách thuê sân phải trả là: {tien_thue} đồng")
else:
    print("Giờ bắt đầu và giờ kết thúc không hợp lệ. Vui lòng nhập lại trong khoảng 5 đến 22.")
