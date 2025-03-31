# Nhập giá trị n (kích thước ma trận)
n = int(input("Nhập bậc ma trận đơn vị: "))

# Tạo ma trận đơn vị
matrix = []

for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(1)  # Đặt giá trị 1 trên đường chéo chính
        else:
            row.append(0)  # Các phần tử còn lại là 0
    matrix.append(row)

# In ma trận đơn vị
print("Ma trận đơn vị:")
for row in matrix:
    print(row)
