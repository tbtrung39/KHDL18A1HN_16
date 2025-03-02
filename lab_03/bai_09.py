n=int(input("Nhap so nguyen duong n: "))
s4=0
s5=0
s6=0
if n<=0:
    print("Khong hop le, vui long nhap so nguyen duong! ")
else:
    for i in range(1,n+1):
        s4+=i**2
        if i%2!=0:
            s5+=i**3
        else:
            s6+=i**4
    print("S4=",s4)
    print("S5=",s5)
    print("S6=",s6)