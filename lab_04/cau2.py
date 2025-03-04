#a,
n = int(input("Nhập n: "))
S = 0
i = 2  # Bắt đầu từ 2
while i <= n:
    S += 1 / i
    i += 1
print("Tổng S11 =", S)
#b,
n = int(input("Nhập n: "))
S = 0
i = 2
while i <= n:
    S += 1 / (i * (i + 1))
    i += 1
print("Tổng S22 =", S)
#c,
import math
n = int(input("Nhập n: "))
S = 0
i = 2
while i <= n:
    S += 1 / math.sqrt(i)
    i += 1
print("Tổng S33 =", S)
