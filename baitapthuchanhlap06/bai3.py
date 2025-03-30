danh_sach = []
while True:
    so = int(input("Nhập số (nhập 0 để kết thúc): "))
    if so == 0:
        break
    danh_sach.append(so)
duong = [so for so in danh_sach if so > 0]
am_va_khong = [so for so in danh_sach if so <= 0]
danh_sach = duong + am_va_khong
print("Danh sách sau khi chuyển số dương lên đầu:", danh_sach)
m = int(input("Nhập số m: "))
danh_sach = [m] + danh_sach
danh_sach.append(m)
count = 0
for _ in danh_sach:
    count += 1
if count >= 5:
    danh_sach = danh_sach[:4] + [m] + danh_sach[4:]

print("Danh sách sau khi chèn m:", danh_sach)