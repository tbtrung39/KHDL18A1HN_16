# Bài 8: Tính tổng các dãy số theo công thức
n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập lại n: "))

S1 = 0
i = 1
while i <= n:
    S1 = S1 + i
    i = i + 1
print("S1 =", S1)

S2 = 0
i = 1
while i <= 2 * n + 1:
    S2 = S2 + i
    i = i + 2
print("S2 =", S2)

S3 = 0
i = 2
while i <= 2 * n:
    S3 = S3 + i
    i = i + 2
print("S3 =", S3)