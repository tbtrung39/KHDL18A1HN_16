# Hàm kiểm tra số nguyên tố
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Nhập số n từ bàn phím
n = int(input("Nhập số n: "))

# Tìm n số nguyên tố đầu tiên
prime_numbers = []
num = 2  # Số bắt đầu kiểm tra
while len(prime_numbers) < n:
    if is_prime(num):
        prime_numbers.append(num)
    num += 1

# In kết quả
print(f"{n} số nguyên tố đầu tiên là:", prime_numbers)