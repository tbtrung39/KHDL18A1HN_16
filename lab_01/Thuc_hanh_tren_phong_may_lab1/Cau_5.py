# Nhập vào số chiều của vector
n = int(input("Nhập số chiều của vector a và b: "))

# Nhập các phần tử của vector a
a = []
print("Nhập các phần tử của vector a:")
for i in range(n):
    a.append(float(input(f"a[{i+1}] = ")))

# Nhập các phần tử của vector b
b = []
print("Nhập các phần tử của vector b:")
for i in range(n):
    b.append(float(input(f"b[{i+1}] = ")))

# Tính tích vô hướng
tich_vo_huong = 0
for i in range(n):
    tich_vo_huong += a[i] * b[i]

# In kết quả
print(f"Tích vô hướng của 2 vector a và b là: {round(tich_vo_huong, 2)}")