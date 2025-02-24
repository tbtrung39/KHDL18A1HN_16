def tinh_tien_thue_san(gio_bat_dau, gio_ket_thuc):
    gio_thue = gio_ket_thuc - gio_bat_dau
    if gio_thue <= 3:
        tien_thue = gio_thue * 100000
    else:
        tien_thue = 3 * 100000 + (gio_thue - 3) * 75000
    if 11 <= gio_bat_dau <= 15 or 11 <= gio_ket_thuc <= 15:
        tien_thue *= 0.9
    return tien_thue
try:
    gio_bat_dau = int(input("Nhap gio bat dau (5-22): "))
    gio_ket_thuc = int(input("Nhap gio ket thuc (5-22): "))
    if 5 <= gio_bat_dau <= gio_ket_thuc <= 22:
        tien_thue = tinh_tien_thue_san(gio_bat_dau, gio_ket_thuc)
        print(f"So tien thue san phai tra la: {tien_thue} dong")
    else:
        print("Gio bat dau va gio ket thuc phai trong khoang tu 5 den 22 gio.")
except ValueError:
    print("Vui long nhap mot so nguyen hop le.")