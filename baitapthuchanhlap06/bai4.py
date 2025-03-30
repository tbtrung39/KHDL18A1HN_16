danh_sach = []
while True:
    so = int(input("Nhập số (nhập 0 để kết thúc): "))
    if so == 0:
        break
    danh_sach.append(so)
danh_sach = [1, 2, 3] + danh_sach
danh_sach = danh_sach + [1, 2, 3]
count = 0
for _ in danh_sach:
    count += 1
if count >= 5:
    danh_sach = danh_sach[:4] + [1, 2, 3] + danh_sach[4:]
k = int(input("Nhập vị trí k: "))
if 1 <= k <= count:
    danh_sach_moi = []
    for i in range(count):
        if i != k - 1:
            danh_sach_moi.append(danh_sach[i])
    danh_sach = danh_sach_moi
count = 0
for _ in danh_sach:
    count += 1
for i in range(count):
    for j in range(0, count - i - 1):
        if danh_sach[j] > danh_sach[j + 1]:
            danh_sach[j], danh_sach[j + 1] = danh_sach[j + 1], danh_sach[j]
print("Danh sách tăng dần:", danh_sach)
for i in range(count):
    for j in range(0, count - i - 1):
        if danh_sach[j] < danh_sach[j + 1]:
            danh_sach[j], danh_sach[j + 1] = danh_sach[j + 1], danh_sach[j]
print("Danh sách giảm dần:", danh_sach)