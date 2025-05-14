A = {'Umbala', 3.14, 'xibua', 42, 2.718}
dem_so_nguyen = 0
dem_so_thuc = 0
dem_chuoi_ky_tu = 0
for item in A:
    if isinstance(item, int):
        dem_so_nguyen += 1
    elif isinstance(item, float):
        dem_so_thuc += 1
    elif isinstance(item, str):
        dem_chuoi_ky_tu += 1

print(f"Số phần tử là số nguyên: {dem_so_nguyen}")
print(f"Số phần tử là số thực: {dem_so_thuc}")
print(f"Số phần tử là chuỗi ký tự: {dem_chuoi_ky_tu}")