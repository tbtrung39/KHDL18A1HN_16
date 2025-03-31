import random

A = [random.randint(1, 99999) for _ in range(1000)]

# Cách 1: Sử dụng sorted()
A_sorted_1 = sorted(A)
print("Danh sách A sau khi sắp xếp (sử dụng sorted()):", A_sorted_1)

# Cách 2: Không sử dụng sorted() (sử dụng thuật toán sắp xếp nổi bọt)
A_sorted_2 = A[:]  # Tạo bản sao của A để không thay đổi A gốc
n = len(A_sorted_2)
for i in range(n):
  for j in range(0, n-i-1):
    if A_sorted_2[j] > A_sorted_2[j+1]:
      A_sorted_2[j], A_sorted_2[j+1] = A_sorted_2[j+1], A_sorted_2[j]
print("Danh sách A sau khi sắp xếp (không sử dụng sorted()):", A_sorted_2)
