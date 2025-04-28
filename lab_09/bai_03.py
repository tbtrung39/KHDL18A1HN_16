def luy_thua(a,n):
    if n==0:
        return 1
    else:
        return a*luy_thua(a,n-1)
a,n=map(int,input("Nhap co so va so mu: ").split())
kq=luy_thua(a,n)
print(f"{a}^{n}= {kq}")