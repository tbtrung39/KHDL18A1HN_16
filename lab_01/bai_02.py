sogiay = int(input("Nhap so giay: "))
sophut = int(input("Nhap so phut: "))
sogio = int(input("Nhap so gio: "))
songay = int(input("Nhap so ngay: "))
tong_giay = sogiay + sophut * 60 + sogio * 3600 + songay * 86400
ngay = tong_giay // 86400
giay_con_lai = tong_giay % 86400
gio = giay_con_lai // 3600
giay_con_lai %= 3600
phut = giay_con_lai // 60
giay = giay_con_lai % 60
print(f"{ngay} ngay, {gio} gio, {phut} phut, {giay} giay")