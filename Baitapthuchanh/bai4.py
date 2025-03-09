n = int(input("Nhập n: "))  
print("Các số nguyên tố nhỏ hơn hoặc bằng", n, "là:")

for i in range(2, n + 1):  
    la_so_nguyen_to  = 1   # Giả sử i là số nguyên tố  
    for j in range(2, int(i ** 0.5) + 1):  # Kiểm tra từ 2 đến căn bậc hai của i  
        if i % j == 0:  
            la_so_nguyen_to = 0  # Nếu chia hết thì không phải số nguyên tố  
            break  
    if la_so_nguyen_to:  
        print(i, end=" ")  