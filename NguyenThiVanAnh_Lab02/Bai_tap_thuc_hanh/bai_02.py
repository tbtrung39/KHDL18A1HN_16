a, b, c=map(float,input("Nhap vao he so cua phuong trinh bac 2: "))
if a==0:
    if b==0:
        if c==0:
            print("Phuong trinh co vo so nghiem")
        else:
            print("Phuong trinh vo nghiem")
    else:
        print("Phuong trinh co mot nghiem x=",-c/b)
else:
    delta=b**2 - 4*a*c
    if delta<0:
        print("Phuong trinh vo nghiem thuc")
    if delta==0:
        print("Phuong trinh co nghiem kep x=",-b/(2*a))
    if delta>0:
        x1=(-b+delta**(1/2))/(2*a)
        x2=(-b-delta**(1/2))/(2*a)
        print("Phuong trinh co hai nghiem phan biet: ")
        print("x1=",x1)
        print("x2=",x2)
              