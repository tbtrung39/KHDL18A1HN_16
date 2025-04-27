n = int(input("Nhập n: "))
 # a. Hàm đệ quy tính giai thừa
def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)
 
def tong_a(n):
    if n == 1:
        return 1
    return 1 / giai_thua(n) + tong_a(n - 1)
 
 
 # b
def tong_day_cong(n):
    if n == 1:
        return 1
    tong = n * (n + 1) // 2
    return 1 / tong + tong_day_cong(n - 1)

 # c
import math
def can_long(n):
    if n == 1:
        return math.sqrt(3)
    return math.sqrt(3 * n + can_long(n - 1))
 
 # d
import math
 
def tinh_s(n, i=1):
    if i == n + 1:
        return math.sqrt(i)
    return math.sqrt(i + tinh_s(n, i + 1))
 
print("Tổng a =", tong_a(n))
print("Tổng b =", tong_day_cong(n))
print("Tổng c =", can_long(n))
print("Tổng d =", tinh_s(n))