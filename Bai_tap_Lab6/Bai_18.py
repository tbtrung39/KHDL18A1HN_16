m = int(input("Nhập số hàng (m): "))
n = int(input("Nhập số cột (n): "))
matrix = []
for i in range(m):
    row = list(map(int, input(f"Nhập hàng {i+1} ({n} số cách nhau bằng dấu cách): ").split()))
    matrix.append(row)
total = 0
for row in matrix:
    total += sum(row)
print("Tổng các phần tử của ma trận:", total)