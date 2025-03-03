n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập lại n (n > 0): "))

S4 = 0
i = 1
while i <= n:
    S4 += i ** 2
    i += 1
print("S4 =", S4)

S5 = 0
i = 1
while i <= n:
    S5 += (2 * i - 1) ** 3
    i += 1
print("S5 =", S5)
