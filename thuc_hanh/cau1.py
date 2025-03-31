
a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]


tong_tat_ca = sum(a)
so_duong = [x for x in a if x > 0]
so_luong_duong = len(so_duong)
tong_duong = sum(so_duong)

# In kết quả
print("Tổng các phần tử của danh sách là:", tong_tat_ca)
print("Số lượng số hạng dương trong danh sách là:", so_luong_duong)
print("Tổng các số hạng dương là:", tong_duong)
