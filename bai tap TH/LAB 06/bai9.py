danh_sach = [2, 4, 6, 8, 10]  # Thay đổi danh sách này để kiểm tra
# Kiểm tra tất cả các số trong list là chẵn
assert all(so % 2 == 0 for so in danh_sach), "Danh sách chứa số lẻ!"
print("Tất cả các số trong danh sách đều là số chẵn.")