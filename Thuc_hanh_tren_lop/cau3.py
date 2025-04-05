import random
n = int(input("Nhập số lượng phần tử của tập hợp A: "))
A = {round(random.uniform(0, 100), 2) for _ in range(n)}
min_value = min(A)
max_value = max(A)
sum_value = sum(A)
print(f"Tập hợp A: {A}")
print(f"Phần tử nhỏ nhất: {min_value}")
print(f"Phần tử lớn nhất: {max_value}")
print(f"Tổng các phần tử: {sum_value}")