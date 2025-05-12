import math
def Ucln(a, b):
    """
    Tìm ước chung lớn nhất của 2 số a và b
    """
    while b:
        a, b = b, a % b
    return abs(a)
def Bcnn(a, b):
    """
    Tìm bội chung nhỏ nhất của 2 số a và b
    """
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // Ucln(a, b)
def SumDivisor(n):
    """
    Tính tổng các ước số của n (không tính chính nó)
    """
    if n == 0:
        return 0
    total = 1 if n != 1 else 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i == n // i:
                total += i
            else:
                total += i + n // i
    return total
if __name__ == "__main__":
    print("1. Tìm UCLN và BCNN của 2 số")
    a = int(input("Nhập số thứ nhất: "))
    b = int(input("Nhập số thứ hai: "))
    print(f"UCLN({a}, {b}) = {Ucln(a, b)}")
    print(f"BCNN({a}, {b}) = {Bcnn(a, b)}")
    
    print("\n2. Tính tổng các ước số của một số")
    n = int(input("Nhập số cần tính tổng ước: "))
    print(f"Tổng các ước của {n} (không tính chính nó) là: {SumDivisor(n)}")