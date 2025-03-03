n = int(input("Nhập số n: "))

nguyen_to = True
if n < 2:
    nguyen_to = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            nguyen_to = False
            break

if nguyen_to:
    print(n, "là số nguyên tố.")
else:
    print(n, "không phải là số nguyên tố.")

    so_duoi = -1
    for x in range(n - 1, 1, -1):
        nguyen_to_duoi = True
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                nguyen_to_duoi = False
                break
        if nguyen_to_duoi:
            so_duoi = x
            break

    so_tren = -1
    for x in range(n + 1):
        nguyen_to_tren = True
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                nguyen_to_tren = False
                break
        if nguyen_to_tren:
            so_tren = x
            break

    if so_duoi == -1:
        print("Số nguyên tố gần nhất là:", so_tren)
    elif so_tren == -1:
        print("Số nguyên tố gần nhất là:", so_duoi)
    else:
        if abs(n - so_duoi) <= abs(n - so_tren):
            print("Số nguyên tố gần nhất là:", so_duoi)
        else:
            print("Số nguyên tố gần nhất là:", so_tren)