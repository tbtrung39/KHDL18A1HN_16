import random
import math

def sinh_day_so(n=100):
    so_luong = min(n, 100)
    day = [random.randint(1, 1000) for _ in range(so_luong)]
    print("Dãy số được sinh ra:")
    print(day)
    return day

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def liet_ke_nt_chia_het_cho_7(day):
    ket_qua = [x for x in day if la_so_nguyen_to(x) and x % 7 == 0]
    print("Các số nguyên tố chia hết cho 7:")
    print(ket_qua)
    return ket_qua

def tinh_tong_so_le(day):
    tong = sum(x for x in day if x % 2 != 0)
    print("Tổng các số lẻ trong dãy:", tong)
    return tong

def la_so_chinh_phuong(n):
    can = int(math.isqrt(n))
    return can * can == n

def kiem_tra_chinh_phuong(day):
    chinh_phuong = [x for x in day if la_so_chinh_phuong(x)]
    if chinh_phuong:
        print("Các số chính phương trong dãy:")
        print(chinh_phuong)
    else:
        print("Không có số chính phương trong dãy.")
    return chinh_phuong