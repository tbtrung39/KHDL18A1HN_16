def tinh_tien_dien(so_kw):
    if so_kw <= 100:
        don_gia = 2000
    elif 101 <= so_kw <= 200:
        don_gia = 2500
    elif 201 <= so_kw <= 300:
        don_gia = 3000
    else:
        don_gia = 5000
    return so_kw * don_gia
try:
    so_kw = int(input("Nhap so KW dien tieu thu: "))
    tien_dien = tinh_tien_dien(so_kw)
    print(f"So tien dien phai tra la: {tien_dien} dong")
except ValueError:
    print("Vui long nhap mot so nguyen hop le.")