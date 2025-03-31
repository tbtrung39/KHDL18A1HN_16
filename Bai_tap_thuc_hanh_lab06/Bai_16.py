# Nhập giá trị X và Y
X = int(input("Nhập số X (số hàng): "))
Y = int(input("Nhập số Y (số cột): "))

# Tạo mảng 2 chiều với giá trị phần tử là i * j
matrix = []

for i in range(X):
    row = []
    for j in range(Y):
        row.append(i * j)
    matrix.append(row)

# In mảng 2 chiều
print("Mảng 2 chiều:")
for row in matrix:
    print(row)
