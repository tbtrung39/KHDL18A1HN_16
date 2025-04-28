def giai_thua_kep(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giai_thua_kep(n-2)

n = int(input("Nhập n: "))
print(f"{n}!! =", giai_thua_kep(n))
#tong
def tong_giai_thua_kep(k):
    if k == 1:
        return 1
    else:
        return tong_giai_thua_kep(k-1) + ((-1)**k) * giai_thua_kep(k)

k = int(input("Nhập k (k < 1000): "))
print("Tổng S là:", tong_giai_thua_kep(k))
