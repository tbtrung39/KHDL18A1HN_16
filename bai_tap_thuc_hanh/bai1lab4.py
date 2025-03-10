# Nhập n
n = 0
while n <= 0:
    n = int(input("Nhập n (n > 0): "))

# Tính S4 
S4 = 0
i = 1
while i <= n:
    S4 = S4 + i * i
    i = i + 1
print("S4 =", S4)

# Tính S5 
S5 = 0
j = 1
tong = 0
while tong < n:
    S5 = S5 + j * j * j
    j = j + 2
    tong = tong + 1
print("S5 =", S5)

# Tính S6 
S6 = 0
k = 2
while k <= 2 * n:
    S6 = S6 + k ** 4
    k = k + 2
print("S6 =", S6)