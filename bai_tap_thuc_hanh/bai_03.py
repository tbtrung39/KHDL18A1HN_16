import math
r = float(input("Nhập bán kính của khối trụ: "))
h = float(input("Nhập chiều cao của khối trụ: "))
pi = 3.14
dien_tich_xung_quanh = 2 * pi * r * h
dien_tich_toan_phan = 2 * pi * r * (r + h)
the_tich = pi * r**2 * h
dien_tich_xung_quanh = round(dien_tich_xung_quanh, 2)
dien_tich_toan_phan = round(dien_tich_toan_phan, 2)
the_tich = round(the_tich, 2)
print(f"Diện tích xung quanh: {dien_tich_xung_quanh}")
print(f"Diện tích toàn phần: {dien_tich_toan_phan}")
print(f"Thể tích: {the_tich}")