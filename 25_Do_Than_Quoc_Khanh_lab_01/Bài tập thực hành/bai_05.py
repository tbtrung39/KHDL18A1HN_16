n = int(input("Nhập số phần tử của vector: "))

a = []
b = []
print("Nhập các phần tử của vector a:")
for i in range(n):
    a.append(float(input(f"a[{i}] = ")))
print("Nhập các phần tử của vector b:")
for i in range(n):
    b.append(float(input(f"b[{i}] = ")))
dot_product = 0
for i in range(n):
    dot_product += a[i] * b[i]
print("Tích vô hướng của hai vector là:", dot_product)
