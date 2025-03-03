N = int(input("Nhập N: "))
#PHAN a
S4 = 0
for i in range(1, N + 1):
    S4 += i ** 2
print("S4 =", S4)
#PHAN b
S5 = 0
for i in range(1, N + 1):
    S5 += (2 * i - 1) ** 3
print("S5 =", S5)
#PHAN c
S6 = 0
for i in range(1, N + 1):
    S6 += (2 * i) ** 4
print("S6 =", S6)