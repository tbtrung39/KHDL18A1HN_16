# Danh sách đã cho
a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]

# 1. Tính tổng các phần tử trong danh sách
tong = sum(a)
print("Tổng các phần tử:", tong)

# 2. Đếm số lượng số hạng dương và tính tổng các số hạng dương
so_duong = [x for x in a if x > 0]
count_duong = len(so_duong)
tong_duong = sum(so_duong)
print("Số lượng số hạng dương:", count_duong)
print("Tổng các số hạng dương:", tong_duong)

# 3. Tìm vị trí phần tử âm đầu tiên
vi_tri_am_dau = next((i for i, x in enumerate(a) if x < 0), None)
print("Vị trí phần tử âm đầu tiên:", vi_tri_am_dau if vi_tri_am_dau is not None else "Không có")

# 4. Tìm vị trí phần tử dương cuối cùng
vi_tri_duong_cuoi = next((i for i in range(len(a)-1, -1, -1) if a[i] > 0), None)
print("Vị trí phần tử dương cuối cùng:", vi_tri_duong_cuoi if vi_tri_duong_cuoi is not None else "Không có")

# 5. Tìm phần tử lớn nhất và vị trí của nó
max_value = max(a)
vi_tri_max = [i for i, x in enumerate(a) if x == max_value]
print("Phần tử lớn nhất:", max_value)
print("Vị trí của phần tử lớn nhất:", vi_tri_max)
