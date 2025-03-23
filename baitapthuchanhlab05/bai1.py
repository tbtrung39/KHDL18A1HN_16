chuoi_str = input("Nhập chuỗi ký tự Str: ")
dem = 0  # Hoặc so_luong, tong_so, luot_dem
for ky_tu in chuoi_str:
    if '0' <= ky_tu <= '9':
        dem += 1
print("Số ký tự là số trong chuỗi Str là:", dem)
