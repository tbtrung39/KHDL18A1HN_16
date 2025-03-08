import math
n = 0
while n <= 0:
    n = int(input("Nhập n (n > 0): "))

# a
S_a = 0
i = 1
while i <= n:
    S_a = S_a + 1 / i
    i = i + 1
print("S_a =", S_a)

# b
S_b = 0
j = 1
while j <= n:
    S_b = S_b + 1 / (j * (j + 1))
    j = j + 1
print("S_b =", S_b)

# c
S_c = 0
k = 2
while k <= n:
    S_c = S_c + 1 / math.sqrt(k)
    k = k + 1
print("S_c =", S_c)
