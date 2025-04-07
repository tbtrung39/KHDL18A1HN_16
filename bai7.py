# Bài 7: Tạo 2 tập hợp A, B gồm ký tự và số, in phần tử chung

import random

ds = ['a', 'b', 'c', 'x', 'y', 1, 2, 3, 4, 5, 6, 7]
A = set()
B = set()

# tạo mỗi tập hợp 5 phần tử
while True:
    A.add(random.choice(ds))
    if len(A) == 5:
        break
while True:
    B.add(random.choice(ds))
    if len(B) == 5:
        break

# Tìm phần tử chung
C = set()
for x in A:
    if x in B:
        C.add(x)

print("Tập A:", A)
print("Tập B:", B)
print("Phần tử chung:", C)
