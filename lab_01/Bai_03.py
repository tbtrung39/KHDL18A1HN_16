pi = 3.14
r = float(input("Nhập bán kính của khối trụ: "))
h = float(input("Nhập chiều cao của khối trụ: "))
dien_tich_xung_quanh = 2 * pi * r * h  
dien_tich_toan_phan = dien_tich_xung_quanh + 2 * pi * r ** 2
the_tich = pi * r ** 2 * h  
print("Diện tích xung quanh khối trụ là:", round(dien_tich_xung_quanh, 2))
print("Diện tích toàn phần khối trụ là:", round(dien_tich_toan_phan, 2))
print("Thể tích khối trụ là:", round(the_tich, 2))
