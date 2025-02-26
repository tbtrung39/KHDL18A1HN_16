
n = int(input("Nhập số nguyên dương n: "))
if n <= 1:
    print("Vui lòng nhập một số lớn hơn 1.")
else:
    print("Phân tích thừa số nguyên tố của số ban đầu là: ", end="")
    for i in range(2, n + 1):
        for _ in range(n):
            if n % i == 0:  
                print(i, end=" ")  
                n //= i  
            else:
                break  
        if n == 1:
            break  