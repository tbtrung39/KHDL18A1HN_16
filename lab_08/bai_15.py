
import random
def tao_chuong_trinh(n):
    lst = []
    while len(lst) < n:
        a = int(input("Nhập a:"))
        lst.append(a)
        lst_new = list(filter(lambda x: x % 2 != 0,lst))
        lst_new1 = list(map(lambda x: x**2,lst_new))
    return lst_new1
n = int(input("Nhập n số nguyên: "))
print(tao_chuong_trinh(n))