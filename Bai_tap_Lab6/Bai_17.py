n = int(input("Nhập bậc n của ma trận đơn vị: "))
identity_matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(1 if i == j else 0)
    identity_matrix.append(row)
print("Ma trận đơn vị:")
for row in identity_matrix:
    print(row)