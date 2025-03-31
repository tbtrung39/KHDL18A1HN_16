n = int(input("Nhập số lượng phần tử của danh sách: "))
danh_sach = []
for i in range(n):
  so = int(input(f"Nhập phần tử thứ {i+1}: "))
  danh_sach.append(so)

# Tìm phần tử lớn thứ hai và vị trí của nó
danh_sach_sorted = sorted(danh_sach, reverse=True)
phan_tu_lon_thu_hai = danh_sach_sorted[1]
vi_tri_lon_thu_hai = danh_sach.index(phan_tu_lon_thu_hai)
print(f"Phần tử lớn thứ hai là {phan_tu_lon_thu_hai}, vị trí là {vi_tri_lon_thu_hai}")

# Tính số lượng các số dương liên tiếp nhiều nhất
so_luong_max = 0
so_luong_hien_tai = 0
for so in danh_sach:
  if so > 0:
    so_luong_hien_tai += 1
  else:
    so_luong_max = max(so_luong_max, so_luong_hien_tai)
    so_luong_hien_tai = 0
so_luong_max = max(so_luong_max, so_luong_hien_tai)  # Kiểm tra chuỗi cuối cùng
print(f"Số lượng số dương liên tiếp nhiều nhất là: {so_luong_max}")

# Tính số lượng các số dương liên tiếp có tổng lớn nhất
tong_max = 0
tong_hien_tai = 0
for so in danh_sach:
  if so > 0:
    tong_hien_tai += so
  else:
    tong_max = max(tong_max, tong_hien_tai)
    tong_hien_tai = 0
tong_max = max(tong_max, tong_hien_tai)  # Kiểm tra chuỗi cuối cùng
print(f"Tổng lớn nhất của các số dương liên tiếp là: {tong_max}")