# Câu 9
n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập lại n (n phải > 0): "))

S4 = 0
for i in range(1, n + 1):
    S4 += i ** 2
print("S4 =", S4)


S5 = 0
for i in range(1, n + 2):
    S5 += (2 * i - 1) ** 3
print("S5 =", S5)


S6 = 0
for i in range(1, n + 1):
    S6 += (2 * i) ** 4
print("S6 =", S6)
