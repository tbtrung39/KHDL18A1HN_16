A = input("Nhap tap hop A(cac phan tu cach nhau boi dau phay): ").split(",")
count_int = 0
count_float = 0
count_str = 0
for item in A:
    item = item.strip()
    if item.isdigit():
        count_int += 1
    elif "." in item and item.replace(".", "").isdigit():
        count_float += 1
    else:
        count_str += 1
print("So phan tu la so nguyen:", count_int)
print("So phan tu la so thuc:", count_float)
print("So phan tu la chuoi ky tu:", count_str)