X = int(input("Nhập X: "))
Y = int(input("Nhập Y: "))

matrix = [[i * j for j in range(Y)] for i in range(X)]

print("Ma trận 2D:")
for row in matrix:
    print(row)
