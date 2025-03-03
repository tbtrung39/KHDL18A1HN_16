N = int(input("Nhập N: "))
#PHAN a
S1 = 0
for i in range(1, N + 1):
    S1 += i
print("S1 =", S1)
#PHAN b
S2 = 0
for i in range(1, N + 1):
    S2 += 2 * i - 1
print("S2 =", S2)
#PHAN c
S3 = 0
for i in range(1, N + 1):
    S3 += 2 * i
print("S3 =", S3)