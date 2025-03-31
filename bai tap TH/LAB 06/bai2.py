n = int(input("Nhập số phần tử: "))
danh_sach = []

for i in range(n):
    so = int(input(f"Nhập phần tử thứ {i+1}: "))
    danh_sach.append(so)

# Tìm phần tử lớn thứ hai và vị trí
danh_sach_sap_xep = sorted(set(danh_sach), reverse=True)
if len(danh_sach_sap_xep) > 1:
    so_lon_thu_hai = danh_sach_sap_xep[1]
    vi_tri = [i for i, v in enumerate(danh_sach) if v == so_lon_thu_hai]
else:
    so_lon_thu_hai = None
    vi_tri = []
print("Phần tử lớn thứ hai:", so_lon_thu_hai)
print("Vị trí xuất hiện:", vi_tri)

# Tìm số lượng số dương liên tiếp dài nhất
so_luong_max = 0
dem = 0
for so in danh_sach:
    if so > 0:
        dem += 1
        so_luong_max = max(so_luong_max, dem)
    else:
        dem = 0
print("Số lượng số dương liên tiếp nhiều nhất:", so_luong_max)

# Tìm dãy số dương liên tiếp có tổng lớn nhất
tong_max = 0
tong = 0
day = []
day_max = []
for so in danh_sach:
    if so > 0:
        tong += so
        day.append(so)
        if tong > tong_max:
            tong_max = tong
            day_max = day[:]
    else:
        tong = 0
        day = []
print("Dãy số dương liên tiếp có tổng lớn nhất:", day_max)