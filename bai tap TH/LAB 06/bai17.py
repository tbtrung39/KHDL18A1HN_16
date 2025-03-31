n = int(input("Nhập số bậc của ma trận đơn vị: "))
A = []
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(1)
        else:
            row.append(0)
    A.append(row)
for row in A:
    print(row)