def X(n):
    if n == 0:
        return 1
    tong = 0
    for i in range(n):
        tong += (n-i)**2 * X(i)
    tong += 12 * X(n-1)
    return tong

n = int(input("Nhập n: "))
print(f"Giá trị X_{n} là:", X(n))
