
a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
max_value = max(a)
vi_tri_max_cuoi = len(a) - 1 - a[::-1].index(max_value)
print("Phần tử lớn nhất trong danh sách là:", max_value)
print("Vị trí phần tử lớn nhất cuối cùng trong danh sách là:", vi_tri_max_cuoi)
