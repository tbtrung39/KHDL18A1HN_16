n = int(input("Nhập số tự nhiên n: "))
tap_nguyen_to = set()
so_hien_tai = 2  
while len(tap_nguyen_to) < n:
    is_prime = True  
    if so_hien_tai < 2:
        is_prime = False
    else:
        j = 2
        while j * j <= so_hien_tai:
            if so_hien_tai % j == 0:
                is_prime = False
                break
            j += 1
    if is_prime:
        tap_nguyen_to.add(so_hien_tai)
    so_hien_tai += 1
ds_nguyen_to = sorted(tap_nguyen_to)
print(f"{n} số nguyên tố đầu tiên là:")
for so in ds_nguyen_to:
    print(so, end=" ")
print()  