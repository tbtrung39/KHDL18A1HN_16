# Bài 5: Tạo tập hợp A gồm 5 phần tử ngẫu nhiên từ 0-9

import random

chu_so = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
A = set()

while True:
    x = random.choice(chu_so)
    A.add(x)
    dem = 0
    for _ in A:
        dem += 1
    if dem == 5:
        break

print("Tập hợp A gồm 5 phần tử ngẫu nhiên:", A)
