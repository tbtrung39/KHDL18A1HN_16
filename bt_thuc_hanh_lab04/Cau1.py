# Câu 1
n = int(input("Nhập n từ bàn phím: "))
while n <= 0:
    n = int(input("Vui lòng nhập số nguyên dương n: "))

S4 = 0
S5 = 0
S6 = 0
i = 1

while i <= n:
    S4 += i ** 2
    S5 += (2 * i - 1) ** 3
    S6 += (2 * i) ** 4
    i += 1

print("S4 =", S4)
print("S5 =", S5)
print("S6 =", S6)