ban_kinh = float(input("Nhập bán kính hình trụ: "))
chieu_cao = float(input("Nhập chiều cao hình trụ: "))
pi = 3.14
dien_tich_xung_quanh = 2 * pi * ban_kinh * chieu_cao
dien_tich_toan_phan = dien_tich_xung_quanh + 2 * pi * ban_kinh ** 2
print("Diện tích xung quanh:", round(dien_tich_xung_quanh, 2))
print("Diện tích toàn phần:", round(dien_tich_toan_phan, 2))