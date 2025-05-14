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

with open(r"bai_04\\f_in.dat", 'r') as file_in:
    numbers = [int(line.strip()) for line in file_in]

