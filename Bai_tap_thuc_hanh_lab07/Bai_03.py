import random

n = int(input("Nhập số lượng phần tử: "))
A = set()
i = 0
while i < n:
    num = round(random.uniform(-100, 100), 2)
    A.add(num)
    i += 1

min_val = None
max_val = None
total = 0

for x in A:
    total += x
    if min_val is None or x < min_val:
        min_val = x
    if max_val is None or x > max_val:
        max_val = x

print("Tập hợp A:", A)
print("Min:", min_val)
print("Max:", max_val)
print("Tổng:", total)
