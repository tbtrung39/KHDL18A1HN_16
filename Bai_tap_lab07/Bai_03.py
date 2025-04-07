import random
n = int(input("Nhập số lượng phần tử n: "))
A = {random.uniform(0, 100) for _ in range(n)}
min_val = min(A)
max_val = max(A)
total = sum(A)
print("Tập hợp A:", A)
print("Phần tử nhỏ nhất:", min_val)
print("Phần tử lớn nhất:", max_val)
print("Tổng các phần tử:", total)