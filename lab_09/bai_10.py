
def tinh_X(n):
    if n == 0:
        return 1
    tong = 0
    for i in range(n):
        tong += (n - i) ** 2 * tinh_X(i)
    return tong
n = int(input("Nhap n: "))
print(f"Gia tri X({n})= {tinh_X(n)} ")
