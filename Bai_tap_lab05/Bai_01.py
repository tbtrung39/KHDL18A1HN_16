chuoi = input("Nhập một chuỗi ký tự: ")
dem = 0
for ky_tu in chuoi:
    if ky_tu.isdigit():
        dem += 1
print("Số ký tự là số trong chuỗi:", dem)