a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]

# Tính tổng các phần tử của danh sách
tong = sum(a)
print("Tổng các phần tử:", tong)

# Đếm số lượng các số hạng dương và tổng của các số hạng dương
so_duong = []
for x in a:
    if x > 0:
        so_duong.append(x)
print("Số lượng các số hạng dương:", len(so_duong))
print("Tổng của các số hạng dương:", sum(so_duong))

# Tìm vị trí phần tử âm đầu tiên
vi_tri_am = -1
for i in range(len(a)):
    if a[i] < 0:
        vi_tri_am = i
        break
print("Vị trí phần tử âm đầu tiên:", vi_tri_am)

# Tìm vị trí phần tử dương cuối cùng
vi_tri_duong = -1
for i in range(len(a) - 1, -1, -1):
    if a[i] > 0:
        vi_tri_duong = i
        break
print("Vị trí phần tử dương cuối cùng:", vi_tri_duong)

# Tìm phần tử lớn nhất và vị trí phần tử lớn nhất cuối cùng
max_value = a[0]
for x in a:
    if x > max_value:
        max_value = x
vi_tri_max = []
for i in range(len(a)):
    if a[i] == max_value:
        vi_tri_max.append(i)
print("Phần tử lớn nhất:", max_value)
vi_tri_max_cuoi = vi_tri_max[-1]
print("Phần tử lớn nhất cuối cùng tại vị trí:", vi_tri_max_cuoi)