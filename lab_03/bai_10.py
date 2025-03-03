n = int(input("Nhập số nguyên dương n: "))

if n <= 0:
    print("Không hợp lệ, vui lòng nhập số nguyên dương")
else:
    print("Phân tích thừa số nguyên tố:", end=" ")
    
    for i in range(2, n + 1): 
        while n % i == 0:  
            print(i, end=" ")  
            n //= i 