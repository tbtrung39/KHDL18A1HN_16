import random
def tao_chuong_trinh(n):
    lst = []
    while len(lst) < n:
        a = int(input("Nhập a:"))
        lst.append(a)
    lst_new = list(map(lambda x: x**2, lst))
    return lst_new
n = int(input("Nhập n số nguyên: "))
print(tao_chuong_trinh(n))