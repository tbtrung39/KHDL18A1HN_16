n = int(input("Nhập số tự nhiên n: "))

A = set()
for i in range(2, n+1):
    if n % i == 0:
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            A.add(i)

B = set()
for i in range(2, n):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime and i not in A:
        B.add(i)

print("Tập hợp A (ước nguyên tố của n):", A)
print("Tập hợp B (nguyên tố <n không là ước của n):", B)