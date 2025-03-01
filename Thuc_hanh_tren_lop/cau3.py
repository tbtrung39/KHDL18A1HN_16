n = int(input("Nhập số n: "))
is_prime = True
if n <= 1:
    is_prime = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{n} là số nguyên tố.")
else:
    lower = n - 1
    upper = n + 1
    while True:
        if lower > 1:
            for i in range(2, int(lower**0.5) + 1):
                if lower % i == 0:
                    lower -= 1
                    break
            else:
                print(f"Số nguyên tố gần {n} nhất là {lower}.")
                break
        if upper > 1:
            for i in range(2, int(upper**0.5) + 1):
                if upper % i == 0:
                    upper += 1
                    break
            else:
                print(f"Số nguyên tố gần {n} nhất là {upper}.")
                break
