# xulydaysong.py
import random
import math

def tao_day_so(n=100):
    return [random.randint(0, 999) for _ in range(n)]

def so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def so_chinh_phuong(n):
    return int(math.sqrt(n)) ** 2 == n

def xu_ly_day(day):
    print("Dãy số:", day)
    print("Số nguyên tố chia hết cho 7:", [x for x in day if x % 7 == 0 and so_nguyen_to(x)])
    print("Tổng các số lẻ:", sum(x for x in day if x % 2 == 1))
    chinh_phuong = [x for x in day if so_chinh_phuong(x)]
    if chinh_phuong:
        print("Số chính phương:", chinh_phuong)
    else:
        print("Không có số chính phương trong dãy.")
