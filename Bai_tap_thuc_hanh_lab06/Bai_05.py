import random

# Sinh danh sách A với 1000 số ngẫu nhiên trong khoảng [1, 99999]
A = []
for _ in range(1000):
    A.append(random.randint(1, 99999))

print(A)
