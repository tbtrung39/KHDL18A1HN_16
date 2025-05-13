import math

def tim_ucln(a, b):
    return math.gcd(a, b)

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
print("Ước chung lớn nhất là:", tim_ucln(a, b))