n = int(input("Nhap mot so: "))
so_nguyen_to = []
for num in range(2, n + 1):
    la_nguyen_to = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            la_nguyen_to = False
            break
    if la_nguyen_to:
        so_nguyen_to.append(num)
print(f"Cac so nguyen to nho hon hoac bang {n}: {so_nguyen_to}")