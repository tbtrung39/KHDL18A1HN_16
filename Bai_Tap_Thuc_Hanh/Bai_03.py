def luy_thua(a,n):
    if n == 0:
        return 1
    elif n > 0:
        return a * luy_thua(a,n - 1)
    else:
        return a * 1/luy_thua(a, -n)
a = int(input("Nhập cơ số: "))
n = int(input("Nhập số mũ: "))
print(luy_thua(a,n))
    
