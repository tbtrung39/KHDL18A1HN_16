import random

# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử n: "))

# Tạo tập hợp A với n số thực ngẫu nhiên (giá trị từ 0 đến 100)
A = set()
while len(A) < n:
    A.add(round(random.uniform(0, 100), 2))  # Làm tròn 2 chữ số thập phân

# Tính phần tử nhỏ nhất, lớn nhất, tổng
min_val = min(A)
max_val = max(A)
sum_val = sum(A)

# In kết quả
print("Tập hợp A:", A)
print("Phần tử nhỏ nhất:", min_val)
print("Phần tử lớn nhất:", max_val)
print("Tổng các phần tử:", round(sum_val, 2))