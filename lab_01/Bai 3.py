ban_kinh = float(input("Nhap ban kinh hinh tru: "))
chieu_cao = float(input("Nhap chieu cao hinh tru: "))
pi = 3.14
dien_tich_xq = 2 * pi * ban_kinh * chieu_cao
dien_tich_tp = 2 * pi * ban_kinh * (ban_kinh + chieu_cao)
the_tich = pi * ban_kinh**2 * chieu_cao
print(f"Dien tich xung quanh: {dien_tich_xq:.2f}")
print(f"Dien tich toan phan: {dien_tich_tp:.2f}")
print(f"The tich: {the_tich:.2f}")