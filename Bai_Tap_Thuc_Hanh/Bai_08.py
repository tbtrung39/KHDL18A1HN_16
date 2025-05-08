import math
# Ý a:
def y_a(n):
    if n == 1:
        return 1/(1*2)
    return (1/(n*(n+1))) + y_a(n-1)
# Ý b:
def tinh_giai_thua(n):
    if n == 1:
        return 1
    return n * tinh_giai_thua(n-1)
def tinh_bieu_thuc_b(n):
    if n == 1:
        return 1/1
    return 1/tinh_giai_thua(n) + tinh_bieu_thuc_b(n -1)

# Ý c:
def y_c(n):
    if n == 1:
        return 1
    return math.sqrt(3*n + (y_c(n - 1)))

n = int(input("Nhập n: "))
print(y_a(n))
print(tinh_bieu_thuc_b(n))
print(y_c(n))

