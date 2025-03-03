n=int(input("Nhap so nguyen duong n: "))
s1=0
s2=0
s3=0
if n<=0:
    print("Khong hop le, vui long nhap so nguyen duong! ")
else:
    for i in range(1,n+1):
        s1+=i
        if i%2!=0:
            s2+=i
        else:
            s3+=i
    print("S1=",s1)
    print("S2=",s2)
    print("S3=",s3)