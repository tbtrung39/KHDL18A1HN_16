n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập lại n (n phải > 0): "))


S1 = 0
for i in range(1, n + 1):
    S1 += i
print("S1 =", S1)


S2 = 0
for i in range(1, n + 2):
    S2 += 2 * i - 1
print("S2 =", S2)


S3 = 0
for i in range(1, n + 1):
    S3 += 2 * i
print("S3 =", S3)
