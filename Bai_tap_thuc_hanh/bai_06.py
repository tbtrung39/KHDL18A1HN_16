import math

def tim_bcnn(a, b):
    return abs(a * b) // math.gcd(a, b)

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
print("Bội chung nhỏ nhất là:", tim_bcnn(a, b))
