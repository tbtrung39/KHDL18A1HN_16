def X(n):
    if n == 0:
        return 1
    total = 0
    for i in range(1, n+1):
        total += (i**2) * X(n - i)
    return total
n = int(input("Nhập n (bài 10): "))
print(f"X_{n} =", X(n))