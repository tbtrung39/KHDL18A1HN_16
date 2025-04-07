n = int(input("Nhập số tự nhiên n: "))
primes = []
num = 2

while len(primes) < n:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
    num += 1

print(f"Dãy {n} số nguyên tố đầu tiên:", primes)