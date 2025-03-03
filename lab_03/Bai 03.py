n = int(input("Nhap mot so: "))
la_nguyen_to = n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
if la_nguyen_to:
    print(f"{n} la so nguyen to.")
else:
    duoi, tren = n - 1, n + 1
    while True:
        la_nguyen_to_duoi = duoi > 1 and all(duoi % i != 0 for i in range(2, int(duoi**0.5) + 1))
        la_nguyen_to_tren = all(tren % i != 0 for i in range(2, int(tren**0.5) + 1))  
        if la_nguyen_to_duoi:
            print(f"{n} khong phai la so nguyen to. So nguyen to gan nhat la {duoi}.")
            break
        if la_nguyen_to_tren:
            print(f"{n} khong phai la so nguyen to. So nguyen to gan nhat la {tren}.")
            break
        duoi -= 1
        tren += 1