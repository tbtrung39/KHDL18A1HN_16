n=int(input("Nhap n: "))
#a
def tong_a(n):
    if n==1:
        return 1/(1*2)
    return 1/(n*(n+1))+tong_a(n-1)
print(f"Tong a: {tong_a(n)}")

#b
def giai_thua(n):
    if n==0 or n==1:
        return 1
    return n*giai_thua(n-1)
def tong_b(n):
    if n==1:
        return 1
    return 1/giai_thua(n) + tong_b(n-1)
print("Tong b:",tong_b(n))

#c
import math
def tong_c(n):
    if n==1:
        return math.sqrt(3)
    return math.sqrt(3*n+tong_c(n-1))
print(f"Tong c: {tong_c(n)}")