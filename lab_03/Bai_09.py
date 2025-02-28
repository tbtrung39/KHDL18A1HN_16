# Bài 9: Tính tổng các dãy số mũ bằng vòng lặp for
n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập lại n: "))

S4 = 0
for i in range(1, n + 1):
    S4 = S4 + (i * i)
print("S4 =", S4)

S5 = 0
for i in range(1, 2 * n + 2, 2):
    S5 = S5 + (i * i * i)
print("S5 =", S5)

S6 = 0
for i in range(2, 2 * n + 1, 2):
    S6 = S6 + (i * i * i * i)
print("S6 =", S6)
