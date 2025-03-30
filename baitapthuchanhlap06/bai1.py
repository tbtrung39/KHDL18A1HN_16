a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
tong = sum(a)
print("Tổng các phần tử trong danh sách là:", tong)
so_luong_duong = 0
tong_duong = 0
for so in a:
    if so > 0:
        so_luong_duong += 1
        tong_duong += so
print("Số lượng số hạng dương:", so_luong_duong)
print("Tổng các số hạng dương:", tong_duong)
vi_tri_am_dau_tien = -1  
for i, so in enumerate(a):
    if so < 0:
        vi_tri_am_dau_tien = i
        break

if vi_tri_am_dau_tien != -1:
    print("Vị trí phần tử âm đầu tiên:", vi_tri_am_dau_tien)
else:
    print("Không có phần tử âm trong danh sách.")
vi_tri_duong_cuoi_cung = -1  

for i, so in enumerate(a):
    if so > 0:
        vi_tri_duong_cuoi_cung = i

if vi_tri_duong_cuoi_cung != -1:
    print("Vị trí phần tử dương cuối cùng:", vi_tri_duong_cuoi_cung)
else:
    print("Không có phần tử dương trong danh sách.")
    
phan_tu_lon_nhat = max(a)
vi_tri_lon_nhat_cuoi_cung = -1
for i, so in enumerate(a):
    if so == phan_tu_lon_nhat:
        vi_tri_lon_nhat_cuoi_cung = i
print("Phần tử lớn nhất:", phan_tu_lon_nhat)
print("Vị trí xuất hiện cuối cùng của phần tử lớn nhất:", vi_tri_lon_nhat_cuoi_cung)