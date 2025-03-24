str = input("Nhập chuỗi ký tự: ")
dem = 0
for i in str :
    if i.isdigit():
        dem += 1
print(f"Số ký tự là số là: {dem}")
