n=int(input("Nhập n:"))
# a) 
S_a = 0
i = 2
while i <= n + 1:
    S_a += 1 / i
    i += 1
print("S_a =", S_a)

# b) 
S_b = 0
i = 2
while i <= n + 1:
    S_b += 1 / (i * (i + 1))
    i += 1
print("S_b =", S_b)

# c) 
S_c = 0
i = 2
while i <= n + 1:
    S_c += 1 / (i ** 0.5)
    i += 1
print("S_c =", S_c)