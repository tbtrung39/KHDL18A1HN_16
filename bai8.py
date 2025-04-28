#a
def tinh_s1(n):
    if n == 1:
        return 1 / (1*2)
    else:
        return 1 / (n*(n+1)) + tinh_s1(n-1)

n = int(input("Nhập n: "))
print("Giá trị S1 là:", tinh_s1(n))
#b
def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giai_thua(n-1)

def tinh_s2(n):
    if n == 1:
        return 1
    else:
        return 1 / giai_thua(n) + tinh_s2(n-1)

n = int(input("Nhập n: "))
print("Giá trị S2 là:", tinh_s2(n))
#c
import math

def tinh_s3(n):
    if n == 1:
        return math.sqrt(3)
    elif n == 2:
        return math.sqrt(6 + math.sqrt(3))
    elif n == 3:
        return math.sqrt(9 + tinh_s3(2))
    else:
        return math.sqrt(3*n + tinh_s3(n-1))

n = int(input("Nhập n (n >= 3): "))
print("Giá trị S3 là:", tinh_s3(n))
#d
import math

def tinh_s4(n):
    if n == 1:
        return math.sqrt(2)
    else:
        return math.sqrt(2 + tinh_s4(n-1))

n = int(input("Nhập số lượng dấu căn n: "))
print("Giá trị S là:", tinh_s4(n))
