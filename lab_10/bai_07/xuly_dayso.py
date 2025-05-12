import random
import math

def sinh_day_so():
    ds = [random.randint(1, 500) for _ in range(100)]
    print("Day so vua sinh:")
    print(ds)
    return ds

def so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def so_nguyen_to_chia_het_cho_7(ds):
    ket_qua = [x for x in ds if so_nguyen_to(x) and x % 7 == 0]
    print("Cac so nguyen to chia het cho 7:")
    print(ket_qua)

def tong_so_le(ds):
    tong = sum(x for x in ds if x % 2 != 0)
    print("Tong cac so le trong day:", tong)

def so_chinh_phuong(n):
    can = int(math.sqrt(n))
    return can * can == n

def kiem_tra_chinh_phuong(ds):
    so_cp = [x for x in ds if so_chinh_phuong(x)]
    if so_cp:
        print("Cac so chinh phuong trong day:")
        print(so_cp)
    else:
        print("Khong co so chinh phuong nao trong day.")
