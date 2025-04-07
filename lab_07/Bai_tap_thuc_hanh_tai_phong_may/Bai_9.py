# Hàm kiểm tra số nguyên tố
def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

# a. Nhập số tự nhiên n
n = int(input("Nhập số tự nhiên n: "))

# b. Tạo tập hợp A: Tập hợp các số nguyên tố là ước của n
A = set()
for i in range(1, n + 1):
    if n % i == 0 and is_prime(i):  # Nếu i là ước của n và là số nguyên tố
        A.add(i)

# c. Tạo tập hợp B: Tập hợp các số nguyên tố nhỏ hơn n và không là ước của n
B = set()
for i in range(2, n):  # Duyệt từ 2 đến n-1
    if is_prime(i) and i not in A:  # Nếu i là số nguyên tố và không phải là ước của n
        B.add(i)

# In kết quả
print(f"Tập hợp A (các số nguyên tố là ước của {n}): {A}")
print(f"Tập hợp B (các số nguyên tố nhỏ hơn {n} và không phải là ước của {n}): {B}")