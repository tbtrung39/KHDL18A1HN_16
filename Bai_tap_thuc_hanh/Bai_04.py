n = int(input("Nhập vào số nguyên n: "))  
prime_numbers = []  
for num in range(2, n + 1):  
    is_prime = True  
    for i in range(2, int(num**0.5) + 1):  
        if num % i == 0:  
            is_prime = False  
            break  
    if is_prime:  
        prime_numbers += [num]   
print("Các số nguyên tố từ 2 đến", n, "là:", prime_numbers)  