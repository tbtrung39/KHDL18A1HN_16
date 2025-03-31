import random

# Sinh danh sách A với 1000 số ngẫu nhiên trong khoảng [1, 99999]
A = []
for _ in range(1000):
    A.append(random.randint(1, 99999))

# Sắp xếp bằng hàm sorted()
sorted_A = sorted(A)
print("Danh sách sau khi sắp xếp với sorted():", sorted_A)

# Sắp xếp không dùng hàm sorted()
for i in range(len(A)):
    for j in range(i + 1, len(A)):
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]

print("Danh sách sau khi sắp xếp không dùng hàm sorted():", A)
