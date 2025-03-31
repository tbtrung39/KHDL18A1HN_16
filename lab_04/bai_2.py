
n=int(input("Nhap so nguyen duong n: "))
i=1
s1=0
s2=0
s3=0
if n<0:
    print("Vui long nhap so nguyen duong!")
else:
    while i<=n:
        s2+=1/(i*(i+1))
        s3+=1/(i**(1/2))
        if i%2==0:
            s1-=1/i
        else:
            s1+=1/i
        i+=1
    print(f"S1={s1}\nS2={s2}\nS3={s3-1}")
