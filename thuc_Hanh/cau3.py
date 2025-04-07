import random
n = int(input("Nhập số lượng phần tử: "))
A = set()
for _ in range(n):
    A.add(random.randint(1, 100))

print("Tập A:", A)
print("Nhỏ nhất:", min(A))
print("Lớn nhất:", max(A))
print("Tổng:", sum(A))
