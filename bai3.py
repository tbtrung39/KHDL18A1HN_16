# Bài 3: Sinh tập hợp A có n phần tử ngẫu nhiên

n = int(input("Nhập số lượng phần tử n: "))
A = set()

print("Nhập", n, "số nguyên (không trùng):")
dem = 0
while dem < n:
    x = int(input(f"Phần tử {dem+1}: "))
    if x not in A:
        A.add(x)
        dem += 1

# Tìm min, max, tổng (không dùng hàm)
min_val = None
max_val = None
tong = 0

for x in A:
    if min_val is None or x < min_val:
        min_val = x
    if max_val is None or x > max_val:
        max_val = x
    tong += x

print("Tập hợp A:", A)
print("Giá trị nhỏ nhất:", min_val)
print("Giá trị lớn nhất:", max_val)
print("Tổng các phần tử:", tong)
