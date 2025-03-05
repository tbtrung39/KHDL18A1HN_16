# Nhập n từ bàn phím
n = int(input("Nhập n: "))

# Duyệt qua tất cả các số từ 2 đến n
for num in range(2, n + 1):
    la_nguyen_to = True  # Giả sử num là số nguyên tố

    # Kiểm tra num có phải số nguyên tố không
    for i in range(2, num):
        if num % i == 0:  # Nếu có ước số khác 1 và chính nó
            la_nguyen_to = False
            break  # Không cần kiểm tra tiếp

    # Nếu num là số nguyên tố, in ra
    if la_nguyen_to:
        print(num, end=" ")