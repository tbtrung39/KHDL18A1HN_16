n = int(input("Nhập một số tự nhiên n: "))
if n <= 0:
    print("n phải là số tự nhiên lớn hơn 0!")
else:
    A = set()
    i = 1
    while i <= n:
        if n % i == 0:
            A.add(i)
        i += 1
    all_numbers = set()
    j = 2
    while j < n:
        all_numbers.add(j)
        j += 1
    primes = set()
    for num in all_numbers:
        is_prime = True
        k = 2
        while k * k <= num:
            if num % k == 0:
                is_prime = False
                break
            k += 1
        if is_prime:
            primes.add(num)
    B = primes - A
    print("Tập hợp A (các ước của n):", A)
    print("Tập hợp B (số nguyên tố nhỏ hơn n và không là ước của n):", B)