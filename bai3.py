danh_sach = []
while True:
  so = int(input("Nhập số (nhập 0 để dừng): "))
  if so == 0:
    break
  danh_sach.append(so)

# Chuyển các phần tử dương lên đầu danh sách
danh_sach_duong = [so for so in danh_sach if so > 0]
danh_sach_am = [so for so in danh_sach if so <= 0]
danh_sach_moi = danh_sach_duong + danh_sach_am
print("Danh sách sau khi chuyển:", danh_sach_moi)

# Chèn một số m vào đầu, cuối và vị trí thứ 5 của danh sách
m = int(input("Nhập số m: "))
danh_sach_moi.insert(0, m)
danh_sach_moi.append(m)
danh_sach_moi.insert(5, m)
print("Danh sách sau khi chèn:", danh_sach_moi)