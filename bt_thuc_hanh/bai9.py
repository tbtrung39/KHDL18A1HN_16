n = int(input("Nhập n: "))
for _ in range(n):
    if n > 0:
        break
    n = int(input("Vui lòng nhập n dương: "))

S4 = 0
for i in range(1, n + 1):
    S4 += i ** 2
print("S4:", S4)

S5 = 0
for i in range(1, n + 1):
    S5 += i ** 3
print("S5:", S5)

S6 = 0
for i in range(2, 2 * n + 1, 2):
    S6 += i ** 4
print("S6:", S6)
