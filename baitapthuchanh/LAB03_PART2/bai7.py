N = int(input("Nhập N: "))
S = 0
for i in range(1, N + 1):
    S += 1 / i
print(round(S, 3)) 