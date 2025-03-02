n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập lại n (n > 0): "))

S1 = n * (n + 1) // 2  # Công thức tính nhanh
print("S1 =", S1)

S2 = 0
i = 1
while i <= n:
    S2 += 2 * i - 1
    i += 1
print("S2 =", S2)

S3 = 0
i = 1
while i <= n:
    S3 += 2 * i
    i += 1
print("S3 =", S3)
