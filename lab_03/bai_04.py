n=int(input("Nhap n: "))
if n<2:
    print("Khong co so nguyen to nao nho hon hoac bang",n)
else:
    print("Cac so nguyen to nho hon hoac bang",n,"la: ")
    for i in range(2,n+1):
        kt=True
        for j in range(2,i):
            if i%j==0:
                kt=False
                break
        if kt:
            print(i,end=" ")