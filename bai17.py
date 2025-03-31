# Nhập số hàng và số cột
m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))

# Nhập danh sách 1D
lst = list(map(int, input("Nhập danh sách số nguyên: ").split()))

# Kiểm tra độ dài danh sách
if len(lst) != m * n:
    print("Số phần tử không hợp lệ!")
else:
    # Chuyển thành ma trận
    matrix = []
    index = 0
    for i in range(m):
        row = []
        for j in range(n):
            row.append(lst[index])
            index += 1
        matrix.append(row)

    # In ma trận
    print("Ma trận:")
    for row in matrix:
        print(row)
