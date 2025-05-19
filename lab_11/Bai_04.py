def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

def prime_divisors(n):
    return sorted(set(i for i in range(2, n+1) if n % i == 0 and is_prime(i)))

with open("f_in.dat", "r") as f:
    nums = [int(line.strip()) for line in f]

with open("f_out.dat", "w") as f:
    for num in nums:
        primes = prime_divisors(num)
        f.write(" ".join(map(str, primes)) + "\n")