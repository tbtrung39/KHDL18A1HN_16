def is_prime(num):
    """Kiểm tra xem một số có phải là số nguyên tố không."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def find_factors(n):
    """Tìm các ước của n."""
    return [i for i in range(1, n + 1) if n % i == 0]
# a
n = int(input("Nhập số tự nhiên n: "))
# b. 
factors = find_factors(n)
A = {x for x in factors if is_prime(x)}
B = {x for x in range(2, n) if is_prime(x) and x not in factors}
print(f"Tập hợp A (các số nguyên tố là ước của {n}): {A}")
print(f"Tập hợp B (các số nguyên tố nhỏ hơn {n} và không là ước của {n}): {B}")