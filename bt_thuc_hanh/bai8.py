n = int(input("Nhập n: "))
for _ in range(n):
    if n > 0:
        break
    n = int(input("Vui lòng nhập n dương: "))

S1 = 0
for i in range(1, n + 1):
    S1 += i
print("S1:", S1)

S2 = 0
for i in range(1, n + 1, 2):
    S2 += i
print("S2:", S2)

S3 = 0
for i in range(2, 2 * n + 1, 2):
    S3 += i
print("S3:", S3)
