import random
n = int(input("Nhập số lượng phần tử n: "))
A = [random.uniform(-100, 100) for i in range(n)]
print("Tập hợp A:", A)
min_A = min(A)
max_A = max(A)
tong = sum(A)
print("Phần tử nhỏ nhất:", min_A)
print("Phần tử lớn nhất:", max_A)
print("Tổng các phần tử:", tong)