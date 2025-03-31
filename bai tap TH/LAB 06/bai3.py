danh_sach = []
while True:
    so = int(input("Nhập số (nhập 0 để dừng): "))
    if so == 0:
        break
    danh_sach.append(so)

so_duong = [x for x in danh_sach if x > 0]
so_khac = [x for x in danh_sach if x <= 0]
danh_sach = so_duong + so_khac
print("Danh sách sau khi chuyển số dương lên đầu:", danh_sach)

m = int(input("Nhập số m cần chèn: "))
danh_sach.insert(0, m)
danh_sach.append(m)
if len(danh_sach) >= 5:
    danh_sach.insert(4, m)
else:
    danh_sach.append(m)
print("Danh sách sau khi chèn m:", danh_sach)