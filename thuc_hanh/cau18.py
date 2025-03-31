m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))

matrix = []
print("Nhập các phần tử của ma trận:")
for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

# Tính tổng các phần tử trong ma trận
total = sum(sum(row) for row in matrix)

print("Ma trận đã nhập:")
for row in matrix:
    print(row)

print("Tổng các phần tử của ma trận:", total)
