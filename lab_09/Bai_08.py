###a)
def tinh_s_a(n):
    if n == 1:
        return 1 / (1 * 2)
    return 1 / (n * (n + 1)) + tinh_s_a(n - 1)
n = int(input("Nhập n: "))
print("Tổng S (phần a) =", tinh_s_a(n))



###b)
def giai_thua(k):
    if k == 0 or k == 1:
        return 1
    return k * giai_thua(k - 1)
def tinh_s_b(n):
    if n == 1:
        return 1
    return 1 / giai_thua(n) + tinh_s_b(n - 1)
n = int(input("Nhập n: "))
print("Tổng S (phần b) =", tinh_s_b(n))


###c)
import math
def tinh_s_c(n):
    if n == 1:
        return math.sqrt(3)
    return math.sqrt(3 * n + tinh_s_c(n - 1))
n = int(input("Nhập n: "))
print("Kết quả S (phần c) =", tinh_s_c(n))



