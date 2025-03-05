# Nhập số n từ bàn phím
n = int(input("Nhập n: "))

# Biến kiểm tra số nguyên tố
la_nguyen_to = True

# Kiểm tra n có phải số nguyên tố không
if n < 2:
    la_nguyen_to = False
else:
    for i in range(2, n):
        if n % i == 0:
            la_nguyen_to = False
            break  # Dừng sớm nếu tìm thấy ước số

# Nếu n là số nguyên tố, in ra kết quả
if la_nguyen_to:
    print("Đây là số nguyên tố.")
else:
    print("Đây không phải số nguyên tố.")

    # Tìm số nguyên tố nhỏ hơn gần nhất
    so_truoc = 0
    for num in range(n - 1, 1, -1):  # Duyệt ngược từ n-1 về 2
        la_nguyen_to = True
        for i in range(2, num):
            if num % i == 0:
                la_nguyen_to = False
                break
        if la_nguyen_to:
            so_truoc = num
            break

    # Tìm số nguyên tố lớn hơn gần nhất
    so_sau = 0
    for num in range(n + 1, 2 * n):  # Duyệt xuôi từ n+1 đến 2n (giới hạn an toàn)
        la_nguyen_to = True
        for i in range(2, num):
            if num % i == 0:
                la_nguyen_to = False
                break
        if la_nguyen_to:
            so_sau = num
            break

    # In số nguyên tố gần nhất
    if (n - so_truoc) <= (so_sau - n):
        print("Số nguyên tố gần nhất là:", so_truoc)
    else:
        print("Số nguyên tố gần nhất là:", so_sau)