# Nhập số bậc n của ma trận đơn vị
n = int(input("Nhập bậc của ma trận đơn vị (n): "))

# Tạo ma trận đơn vị bậc n (Identity Matrix)
A = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

# In kết quả
for row in A:
    print(row)