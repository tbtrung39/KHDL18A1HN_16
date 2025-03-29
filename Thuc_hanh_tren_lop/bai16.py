X, Y = map(int, input("Nhập X và Y (cách nhau bởi dấu cách): ").split())
matrix = [[i * j for j in range(Y)] for i in range(X)]
for row in matrix:
    print(row)
