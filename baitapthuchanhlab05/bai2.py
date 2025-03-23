chuoi_str = input("Nhập chuỗi ký tự Str: ")
dem = 0
for ky_tu in chuoi_str:
    if not ('a' <= ky_tu <= 'z' or 'A' <= ky_tu <= 'Z' or '0' <= ky_tu <= '9'):
        dem += 1
print("Số ký tự không phải chữ cái tiếng Anh và không phải số trong chuỗi Str là:", dem)