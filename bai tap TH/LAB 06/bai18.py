# Nhập kích thước ma trận
m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))
A = []
# Nhập ma trận từ bàn phím
print(f"Nhập các phần tử cho ma trận {m}x{n}:")
for i in range(m):
    row = []
    for j in range(n):
        value = int(input(f"Nhập phần tử A[{i+1}][{j+1}]: "))
        row.append(value)
    A.append(row)
# Tính tổng các phần tử của ma trận
sum_A = sum(sum(row) for row in A)
print("Ma trận A vừa nhập:")
for row in A:
    print(row)
print(f"Tổng các phần tử của ma trận A: {sum_A}")