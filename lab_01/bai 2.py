d = int(input("Nhap so ngay: "))
h = int(input("Nhap so gio: "))
m = int(input("Nhap so phut: "))
s = int(input("Nhap so giay: "))
tong_so_giay = d * 24 * 3600 + h * 3600 + m * 60 + s
print(f"Tong so giay: {tong_so_giay}")