n = int(input("Nhập số nguyên dương n: "))
if n <= 1:
    print("Số nguyên dương phải lớn hơn 1.")
else:
    print(f"Phân tích thừa số nguyên tố của {n}:")
    i=2 
    for i in range(2, n + 1):  
        if n % i == 0: 
            print(i, end=" ")  
            n //= i
            i -= 1
    print()  