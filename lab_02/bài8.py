def tinh_luong(TNCT):
    luong_can_ban = 1350000
    if TNCT < 12:
        he_so = 2.34
    elif 12 <= TNCT < 36:
        he_so = 3.33
    elif 36 <= TNCT < 60:
        he_so = 3.66
    else:
        he_so = 3.99
    return he_so * luong_can_ban
try:
    TNCT = int(input("Nhap tham nien cong tac (thang): "))
    luong = tinh_luong(TNCT)
    print(f"Luong cua nhan vien la: {luong} dong")
except ValueError:
    print("Vui long nhap mot so nguyen hop le.")