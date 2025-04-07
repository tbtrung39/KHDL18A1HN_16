n = int(input("Nhập số tự nhiên n: "))
if n <= 0:
    print("Vui lòng nhập một số tự nhiên dương.")
else:
    danh_sach_nguyen_to = []
    so_hien_tai = 2

    while len(danh_sach_nguyen_to) < n:
        la_nguyen_to = True 
        for i in range(2, int(so_hien_tai ** 0.5) + 1):
            if so_hien_tai % i == 0:
                la_nguyen_to = False
                break
        if la_nguyen_to:
            danh_sach_nguyen_to.append(so_hien_tai)
        so_hien_tai += 1
    print(f"Dãy {n} số nguyên tố đầu tiên là:", danh_sach_nguyen_to)