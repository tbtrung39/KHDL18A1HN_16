n = int(input("Nhập số hàng của tam giác: "))

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")  # In khoảng trắng để canh giữa
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == n - 1:
            print("*", end="")  # In sao ở viền
        else:
            print(" ", end="")  # Phần bên trong rỗng
    print()
