# Nhập giá trị X, Y
X = int(input("Nhập X: "))
Y = int(input("Nhập Y: "))

# Khởi tạo ma trận
matrix = []
for i in range(X):
    row = []
    for j in range(Y):
        row.append(i * j)
    matrix.append(row)

# In kết quả
print("Ma trận:")
for row in matrix:
    print(row)
