import math

#a
def tinh_Sa(n):
    if n == 1:
        return 1 / (1 * 2)
    return 1 / (n * (n + 1)) + tinh_Sa(n - 1)

#b
def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)

def tinh_Sb(n):
    if n == 1:
        return 1
    return 1 / giai_thua(n) + tinh_Sb(n - 1)

#c
def tinh_Sc(n):
    if n == 1:
        return math.sqrt(3)
    return math.sqrt(3 * n + tinh_Sc(n - 1))

#d
def tinh_Sd(n):
    if n == 1:
        return math.sqrt(1)
    return math.sqrt(n + tinh_Sd(n - 1))

n = int(input("Nhập n: "))
print("Kết quả S (a):", tinh_Sa(n))
print("Kết quả S (b):", tinh_Sb(n))
print("Kết quả S (c):", tinh_Sc(n))
print("Kết quả S (d):", tinh_Sd(n))
