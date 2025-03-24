str = input("Nhập chuỗi ký tự: ")
dem = 0
for i in str:
    if i.isdigit():
        continue
    if i.isalpha():
        continue
    else :
        dem += 1
print(f"Số ký tự không phải số và chữ là: {dem}")