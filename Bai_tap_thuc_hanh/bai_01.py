# Danh sách đã cho
a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]

# 1
tong = 0
for phan_tu in a:
    tong += phan_tu
print("Tổng các phần tử của danh sách:", tong)

# 2
so_luong_duong = 0
tong_duong = 0
for phan_tu in a:
    if phan_tu > 0:
        so_luong_duong += 1
        tong_duong += phan_tu
print("Số lượng số dương:", so_luong_duong)
print("Tổng các số dương:", tong_duong)

# 3
vi_tri_am_dau_tien = -1  
for i in range(len(a)):
    if a[i] < 0:
        vi_tri_am_dau_tien = i
        break  
if vi_tri_am_dau_tien != -1:
    print("Vị trí phần tử âm đầu tiên:", vi_tri_am_dau_tien)
else:
    print("Không có phần tử âm trong danh sách.")

# 4
vi_tri_duong_cuoi_cung = -1 
for i in range(len(a)):
    if a[i] > 0:
        vi_tri_duong_cuoi_cung = i
if vi_tri_duong_cuoi_cung != -1:
    print("Vị trí phần tử dương cuối cùng:", vi_tri_duong_cuoi_cung)
else:
    print("Không có phần tử dương trong danh sách.")

# 5
phan_tu_lon_nhat = a[0]
vi_tri_lon_nhat_cuoi_cung = 0
for i in range(len(a)):
    if a[i] >= phan_tu_lon_nhat:
        phan_tu_lon_nhat = a[i]
        vi_tri_lon_nhat_cuoi_cung = i
print("Phần tử lớn nhất:", phan_tu_lon_nhat)
print("Vị trí phần tử lớn nhất cuối cùng:", vi_tri_lon_nhat_cuoi_cung)