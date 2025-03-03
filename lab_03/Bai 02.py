n = int(input("Nhap mot so: "))
so_hoan_hao = []
for num in range(2, n):
    tong_uoc_so = 1
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            tong_uoc_so += i
            if i != num // i:
                tong_uoc_so += num // i
    if tong_uoc_so == num:
        so_hoan_hao.append(num)
print(f"Cac so hoan hao nho hon {n}: {so_hoan_hao}")