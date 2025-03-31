import random

# 1. Sinh danh sách A gồm 1000 số tự nhiên ngẫu nhiên trong khoảng [1, 99999]
A = [random.randint(1, 99999) for _ in range(1000)]
print("Danh sách A ban đầu:", A[:20], "...")  # In 20 phần tử đầu để kiểm tra

# 2. Sắp xếp danh sách A theo thứ tự tăng dần bằng sorted()
sorted_A = sorted(A)
print("Danh sách sau khi sắp xếp (dùng sorted()):", sorted_A[:20], "...")

# 3. Sắp xếp danh sách A không dùng sorted() (Dùng Bubble Sort)
A_copy = A[:]  # Tạo bản sao để tránh ảnh hưởng đến danh sách gốc
n = len(A_copy)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if A_copy[j] > A_copy[j + 1]:  # Hoán đổi nếu phần tử trước lớn hơn phần tử sau
            A_copy[j], A_copy[j + 1] = A_copy[j + 1], A_copy[j]

print("Danh sách sau khi sắp xếp (Bubble Sort):", A_copy[:20], "...")