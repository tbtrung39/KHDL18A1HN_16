n = int(input("Nhập số n :"))
if n<2:
    print("không có nguyên tố nào nhỏ hơn hoặc bằng",n)
else:
    print("các sô nguyên tố nhỏ hơn hoặc bằng",n,"là")
    for i in range (2,n+1):
        so_nguyen_to=True
        for j in range (2,int(i**0.5)+1):
            if i % j ==0:
             so_nguyen_to =False
            break
        if so_nguyen_to:
            print(i, end="")