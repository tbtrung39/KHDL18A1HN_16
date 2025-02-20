
n = int(input("Nhập kích thước của các vector: "))
a = []
for i in range(n):
    a.append(float(input(f"Nhập phần tử thứ {i + 1} của vector a: ")))
b = []
for i in range(n):
    b.append(float(input(f"Nhập phần tử thứ {i + 1} của vector b: ")))
tich_vo_huong = sum(a[i] * b[i] for i in range(n))
print(f"Tích vô hướng của hai vector là: {tich_vo_huong}")
