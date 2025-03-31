danh_sach_1 = [2, 4, 6, 8, 10]
danh_sach_2 = [1, 2, 3, 4, 5]

# Kiểm tra danh sách 1
for so in danh_sach_1:
  assert so % 2 == 0, f"Số {so} trong danh sách 1 không phải là số chẵn"
print("Tất cả số trong danh sách 1 đều là số chẵn")

# Kiểm tra danh sách 2
for so in danh_sach_2:
  assert so % 2 == 0, f"Số {so} trong danh sách 2 không phải là số chẵn"
print("Tất cả số trong danh sách 2 đều là số chẵn")