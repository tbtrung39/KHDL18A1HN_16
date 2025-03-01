n = int(input("Nhập số nguyên dương: "))
if n <= 1:
    print("Vui lòng nhập số nguyên dương lớn hơn 1.")
else:
    print(f"Phân tích thừa số nguyên tố của {n} là:", end=" ")
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(i, end=" ")
            n //= i
            break 
    for i in range(i, int(n**0.5) + 1):
        if n % i == 0:
            print(i, end=" ")
            n //= i
    if n > 2:
        print(n)
