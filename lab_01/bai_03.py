pi = 3.14
r = float(input("Nhập bán kính r: "))
h = float(input("Nhập chiều cao h: "))
dien_tich_xung_quanh = 2 * pi * r * h
dien_tich_toan_phan = 2 * pi * r * (r + h)
the_tich = pi * r**2 * h
print(f"Diện tích xung quanh: {round(dien_tich_xung_quanh, 2)}")
print(f"Diện tích toàn phần: {round(dien_tich_toan_phan, 2)}")
print(f"Thể tích: {round(the_tich, 2)}")
