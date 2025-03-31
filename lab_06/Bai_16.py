# Nhập giá trị X và Y từ người dùng
X = int(input("Nhập số hàng (X): "))
Y = int(input("Nhập số cột (Y): "))

# Tạo mảng 2 chiều với giá trị phần tử là i * j
matrix = [[i * j for j in range(Y)] for i in range(X)]

# In mảng kết quả
for row in matrix:
    print(row)