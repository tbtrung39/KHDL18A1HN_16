#Bước 1(Bài 7):
import random
import math

def sinh_day_so_nguyen(n=100):
    day_so = [random.randint(1, 1000) for _ in range(random.randint(1, n))]
    return day_so

def hien_thi_day_so(day_so):
    print("Dãy số:", day_so)

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def liet_ke_so_nguyen_to_chia_het_cho_7(day_so):
    so_nguyen_to_chia_het_cho_7 = [num for num in day_so if la_so_nguyen_to(num) and num % 7 == 0]
    if so_nguyen_to_chia_het_cho_7:
        print("Các số nguyên tố chia hết cho 7 trong dãy:", so_nguyen_to_chia_het_cho_7)
    else:
        print("Không có số nguyên tố chia hết cho 7 trong dãy.")

def tinh_tong_so_le(day_so):
    tong_so_le = sum(num for num in day_so if num % 2 != 0)
    print("Tổng các số lẻ trong dãy:", tong_so_le)

def la_so_chinh_phuong(n):
    if n < 0:
        return False
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n

def kiem_tra_so_chinh_phuong(day_so):
    so_chinh_phuong = [num for num in day_so if la_so_chinh_phuong(num)]
    if so_chinh_phuong:
        print("Các số chính phương trong dãy:", so_chinh_phuong)
    else:
        print("Không có số chính phương trong dãy.")