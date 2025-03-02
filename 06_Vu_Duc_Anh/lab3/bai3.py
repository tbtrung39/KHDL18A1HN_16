n = int(input("Nhập số n: "))
is_prime = True
i = 2

while i * i <= n:
    if n % i == 0:
        is_prime = False
        break
    i += 1

if is_prime and n > 1:
    print(f"{n} là số nguyên tố.")
else:
    num1, num2 = n - 1, n + 1
    while True:
        is_prime1 = True
        i = 2
        while i * i <= num1 and num1 > 1:
            if num1 % i == 0:
                is_prime1 = False
                break
            i += 1
        if is_prime1 and num1 > 1:
            print(f"Số nguyên tố gần nhất là {num1}")
            break
        
        is_prime2 = True
        i = 2
        while i * i <= num2:
            if num2 % i == 0:
                is_prime2 = False
                break
            i += 1
        if is_prime2:
            print(f"Số nguyên tố gần nhất là {num2}")
            break
        
        num1 -= 1
        num2 += 1
