
n = int(input("Nhập số n: "))
nguyen_to = True
if n < 2:
    nguyen_to = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            nguyen_to = False
            break
if nguyen_to:
    print(n, "là số nguyên tố.")
else:
    duoi = n - 1
    for k in range(n - 1, 1, -1):
        nguyen_to_duoi = True
        for i in range(2, int(k ** 0.5) + 1):
            if k % i == 0:
                nguyen_to_duoi = False
                break
        if nguyen_to_duoi:
            duoi = k
            break
    tren = n + 1
    for k in range(n + 1, 2 * n):  
        nguyen_to_tren = True
        for i in range(2, int(k ** 0.5) + 1):
            if k % i == 0:
                nguyen_to_tren = False
                break
        if nguyen_to_tren:
            tren = k
            break
    if n - duoi <= tren - n:
        print(n, "không phải là số nguyên tố. Số nguyên tố gần nhất là", duoi)
    else:
        print(n, "không phải là số nguyên tố. Số nguyên tố gần nhất là", tren)