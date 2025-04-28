def ucln(a,b):
    if b==0:
        return a
    else:
        return ucln(b,a%b)
def ucln_day_so(n):
    if n==1:
        x=int(input("Nhap so thu 1: "))
        return x
    else:
        x=int(input(f"Nhap so thu {n}:"))
        return ucln(x,ucln_day_so(n-1))
n=int(input("Nhap n: "))
kq=ucln_day_so(n)
print(f"Uoc chung lon nhat cua {n} so do la: {kq}")