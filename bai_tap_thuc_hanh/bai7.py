str=input("Nhap chuoi: ")
so=""
for c in str:
    if c.isdigit():
        so+=c
if so=="":
    print(f"Chuoi {str} khong chua so")
else:
    print("Chuoi so thu duoc la:",so)
    n=int(so)
    tong_uoc=0
    for i in range(1,n):
        if n%i==0:
            tong_uoc+=i
    if tong_uoc==n:
        print(f"{n} la so hoan hao")
    else:
        print(f"{n} khong phai la so hoan hao")