def tinh_X(n):
    if n == 0:
        return 1
    tong = 0
    for k in range(n):
        tong += (n - k) ** 2 * tinh_X(k)
    return tong

n = int(input("Nhập n: "))
print(f"Giá trị X_{n} là:", tinh_X(n))
