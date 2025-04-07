# Bài 9: Nhập tập hợp A, B (số nguyên từ 1-16), in số lượng chung, riêng

A = set()
B = set()

print("Nhập phần tử cho tập hợp A (gõ -1 để kết thúc):")
while True:
    x = int(input("A: "))
    if x == -1:
        break
    if 1 <= x <= 16:
        A.add(x)

print("Nhập phần tử cho tập hợp B (gõ -1 để kết thúc):")
while True:
    x = int(input("B: "))
    if x == -1:
        break
    if 1 <= x <= 16:
        B.add(x)

# Tập chung
C = set()
for x in A:
    if x in B:
        C.add(x)

# Tập A không có trong B
D = set()
for x in A:
    if x not in B:
        D.add(x)

# Đếm phần tử tập C và D
dem_chung = 0
for _ in C:
    dem_chung += 1

dem_riêng = 0
for _ in D:
    dem_riêng += 1

print("Số phần tử chung giữa A và B:", dem_chung)
print("Số phần tử thuộc A mà không thuộc B:", dem_riêng)
