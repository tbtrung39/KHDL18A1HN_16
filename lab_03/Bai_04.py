n = int(input("Nhập giá trị n: "))
print("Các số nguyên tố nhỏ hơn hoặc bằng",n, "là:")
for num in range(2, n + 1):  
    so_nguyen_to = True
    for i in range(2, int(num ** 0.5) + 1):  
        if num % i == 0:
            so_nguyen_to = False
            break
    if so_nguyen_to:
        print(num)