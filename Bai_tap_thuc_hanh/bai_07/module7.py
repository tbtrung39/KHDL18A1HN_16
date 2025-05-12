import random
import math

def sinh_day_so(n=100):
    day_so = [random.randint(1, 100) for _ in range(n)]
    print("Dãy số được sinh ra:")
    print(day_so)
    return day_so

def so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def liet_ke_nguyen_to_chia_het_cho_7(day_so):
    print("Các số nguyên tố chia hết cho 7 trong dãy:")
    for x in day_so:
        if so_nguyen_to(x) and x % 7 == 0:
            print(x, end=' ')
    print()

def tinh_tong_so_le(day_so):
    tong = sum(x for x in day_so if x % 2 == 1)
    print(f"Tổng các số lẻ trong dãy: {tong}")

def kiem_tra_chinh_phuong(day_so):
    co_chinh_phuong = False
    for x in day_so:
        if int(math.sqrt(x)) ** 2 == x:
            co_chinh_phuong = True
            break
    if co_chinh_phuong:
        print("Dãy có chứa số chính phương.")
    else:
        print("Dãy không có số chính phương.")
