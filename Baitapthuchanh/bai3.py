# Nhập số nguyên n
n = int(input("Nhập số nguyên n: "))

# Kiểm tra số nguyên tố
la_so_nguyen_to = 1
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        la_so_nguyen_to = 0 
        break

if la_so_nguyen_to and n > 1:
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải số nguyên tố.")

    # Tìm số nguyên tố gần nhất
    so_nguyen_to_nho_hon = None, so_nguyen_to_lon_hon = None

    # Tìm số nguyên tố nhỏ hơn gần nhất
    for i in range(n-1, 1, -1):
        la_so_nguyen_to = 1
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                la_so_nguyen_to = 0
                break
        if la_so_nguyen_to:
            la_so_nguyen_to_nho_hon = i
            break

    # Tìm số nguyên tố lớn hơn gần nhất
    for i in range(n+1, n*2):  # Giới hạn tìm kiếm để tránh vòng lặp vô hạn
        la_so_nguyen_to = 1 
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                la_so_nguyen_to = 0
                break
        if la_so_nguyen_to:
            la_so_nguyen_to_lon_hon = i
            break

    # Chọn số nguyên tố gần nhất
    if so_nguyen_to_nho_hon is None:
        print(f"Số nguyên tố gần nhất là {so_nguyen_to_lon_hon}.")
    elif so_nguyen_to_lon_hon is None:
        print(f"Số nguyên tố gần nhất là {so_nguyen_to_nho_hon}.")
    else:
        so_nguyen_to_gan_nhat  = so_nguyen_to_nho_hon if abs(n - so_nguyen_to_nho_hon) <= abs(n - so_nguyen_to_lon_hon ) else so_nguyen_to_lon_hon
        print(f"Số nguyên tố gần nhất là {so_nguyen_to_gan_nhat}.")