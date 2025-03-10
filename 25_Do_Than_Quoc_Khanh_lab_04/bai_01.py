n=int(input("Nhap so nguyen duong n: "))
i=1
s4=0
s5=0
s6=0
if n<=0:
    print("Vui long nhap so nguyen duong!")
else:
    while i<=n:
        s4+=i*i
        if i%2!=0:
            s5+=i**3
        else:
            s6+=i**4
        i+=1
    print(s4,s5,s6)