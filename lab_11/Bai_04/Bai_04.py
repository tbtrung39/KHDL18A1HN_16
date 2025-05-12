def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def prime_divisors(n):
    divisors = []
    for i in range(2, n+1):
        if n % i == 0 and is_prime(i):
            divisors.append(i)
    return divisors

with open(r'lab_11\Bai_04\f_in.dat', 'r') as file_in:
    numbers = [int(line.strip()) for line in file_in]


with open('f_out.dat', 'w') as file_out:
    for number in numbers:
        primes = prime_divisors(number)
        line = ' '.join(str(p) for p in primes)
        file_out.write(line + '\n')