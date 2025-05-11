# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Hàm tìm các ước số nguyên tố khác nhau của một số
def prime_factors(n):
    factors = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0 and is_prime(i):
            factors.add(i)
        if n % i == 0 and is_prime(n // i):
            factors.add(n // i)
    if is_prime(n):
        factors.add(n)
    return sorted(factors)

# Đọc dữ liệu từ f_in.dat
with open(r"Thuc_hanh_tren_lop\cau4\f_in.dat", "r") as f:
    numbers = [int(line.strip()) for line in f]

# Ghi kết quả ra f_out.dat
with open("f_out.dat", "w") as f:
    for num in numbers:
        primes = prime_factors(num)
        f.write(" ".join(map(str, primes)) + "\n")
