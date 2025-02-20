U = 220
I = 2.7
t = float(input("Nhap thoi gian su dung (giay): "))
P = U * I
E = P * t
tien_dien = (E / 3600000) * 7000
print("Tien dien phai tra la:", round(tien_dien, 2), "VND")