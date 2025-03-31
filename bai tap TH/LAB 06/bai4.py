danh_sach = []
while True:
    so = int(input("Nhập số tự nhiên (0 để dừng): "))
    if so == 0:
        break
    danh_sach.append(so)

# Chèn [1,2,3] vào đầu, cuối, và vị trí thứ 5 của danh sáchsách
danh_sach = [1, 2, 3] + danh_sach + [1, 2, 3]
if len(danh_sach) >= 5:
    danh_sach = danh_sach[:4] + [1, 2, 3] + danh_sach[4:]
print("Danh sách sau khi chèn:", danh_sach)

# Xóa phần tử ở vị trí k
k = int(input("Nhập vị trí cần xóa: ")) - 1
if 0 <= k < len(danh_sach):
    danh_sach.pop(k)
print("Danh sách sau khi xóa:", danh_sach)

# Sắp xếp tăng dần, giảm dần
print("Danh sách sắp xếp tăng dần:", sorted(danh_sach))
print("Danh sách sắp xếp giảm dần:", sorted(danh_sach, reverse=True))