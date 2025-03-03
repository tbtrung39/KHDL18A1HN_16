n=int(input("Nhap n: "))
if n<=6:
    print("Khong co so hoan hao nao nho hon",n)
else:
    print("Cac so hoan hao nho hon",n,"la: ")
    for i in range(1,n):
        tong_uoc=0
        for j in range(1,i):
            if i%j==0:
                tong_uoc+=j
        if tong_uoc==i:
            print(i,end=" ")