# sohoc.py

def ucln(a, b):
    """Trả về ước chung lớn nhất của a và b."""
    while b:
        a, b = b, a % b
    return a

def bcnn(a, b):
    """Trả về bội chung nhỏ nhất của a và b."""
    return abs(a * b) // ucln(a, b)

def sum_divisor(n):
    """Tính tổng tất cả ước số của n."""
    return sum(i for i in range(1,n))