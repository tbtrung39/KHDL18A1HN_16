# Nhập số hàng và số cột
m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))

# Nhập ma trận
matrix = []
for i in range(m):
    row = list(map(int, input(f"Nhập hàng {i+1}: ").split()))
    matrix.append(row)

# Tính tổng các phần tử
sum_matrix = 0
for row in matrix:
    for element in row:
        sum_matrix += element

# In ma trận và tổng
print("Ma trận A:")
for row in matrix:
    print(row)
print("Tổng các phần tử của ma trận:", sum_matrix)
