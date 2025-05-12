import random
import math

def sinh_day_so(n=100):
    """Sinh ngẫu nhiên tối đa 100 số nguyên từ 1 đến 1000"""
    if n > 100:
        n = 100
    return [random.randint(1, 1000) for _ in range(n)]

def so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def liet_ke_snt_chia_het_7(day):
    return [x for x in day if so_nguyen_to(x) and x % 7 == 0]

def tong_so_le(day):
    return sum(x for x in day if x % 2 != 0)

def so_chinh_phuong(n):
    can = int(math.sqrt(n))
    return can * can == n

def kiem_tra_va_lay_scp(day):
    scp = [x for x in day if so_chinh_phuong(x)]
    return scp