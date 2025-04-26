def giai_thua_kep(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua_kep(n - 2)

def tinh_tong(k):
    S = 0
    for i in range(1, k + 1):
        dau = (-1) ** (i + 1)
        S += dau * giai_thua_kep(i)
    return S


k = int(input("Nhập giá trị k (nhỏ hơn 1000): "))
print("Kết quả S =", tinh_tong(k))