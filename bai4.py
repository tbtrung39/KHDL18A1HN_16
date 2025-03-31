danh_sach = []
while True:
  so = int(input("Nhập số (nhập 0 để dừng): "))
  if so == 0:
    break
  danh_sach.append(so)

# Chèn danh sách [1, 2, 3] vào đầu, cuối và vị trí thứ 5 của danh sách
danh_sach.insert(0, [1, 2, 3])
danh_sach.append([1, 2, 3])
danh_sach.insert(5, [1, 2, 3])
print("Danh sách sau khi chèn:", danh_sach)

# Xóa phần tử thứ k trong danh sách
k = int(input("Nhập vị trí k cần xóa: "))
del danh_sach[k-1]
print("Danh sách sau khi xóa:", danh_sach)

# Sắp xếp danh sách theo thứ tự tăng dần, giảm dần
danh_sach_tang_dan = sorted(danh_sach)
danh_sach_giam_dan = sorted(danh_sach, reverse=True)
print("Danh sách tăng dần:", danh_sach_tang_dan)
print("Danh sách giảm dần:", danh_sach_giam_dan)