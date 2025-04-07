A = input("Nhap tap hop A(cac phan tu cach nhau boi dau phay): ").split(",")
d_int = 0
d_float = 0
d_str = 0
for item in A:
    item = item.strip()
    if item.isdigit():
        d_int += 1
    elif "." in item and item.replace(".", "").isdigit():
        d_float += 1
    else:
        d_str += 1
print("So phan tu la so nguyen:", d_int)
print("So phan tu la so thuc:", d_float)
print("So phan tu la chuoi ky tu:", d_str)