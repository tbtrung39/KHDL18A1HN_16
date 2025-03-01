n = int(input("Nhap n: "))

for so in range(2, n):
    tong_uoc = 0
    for i in range(1, so):
        if so % i == 0:
            tong_uoc += i

    if tong_uoc == so:
        print(so, "la so hoan hao nho hon n")
