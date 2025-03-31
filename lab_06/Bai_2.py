# Nhập số phần tử của danh sách
n = int(input("Nhập số phần tử của danh sách: "))

# Nhập danh sách các số tự nhiên
lst = []
for i in range(n):
    lst.append(int(input(f"Nhập phần tử thứ {i+1}: ")))

# Tìm phần tử lớn thứ hai và vị trí của nó
max1 = max(lst)  # Tìm phần tử lớn nhất
max2 = float('-inf')  # Khởi tạo phần tử lớn thứ hai là -∞
pos2 = -1  # Vị trí của phần tử lớn thứ hai

for i in range(n):
    if lst[i] < max1 and lst[i] > max2:
        max2 = lst[i]
        pos2 = i  # Cập nhật vị trí cuối cùng mà max2 xuất hiện

if max2 == float('-inf'):
    print("Không có phần tử lớn thứ hai trong danh sách.")
else:
    print(f"Phần tử lớn thứ hai là {max2} tại vị trí {pos2}")