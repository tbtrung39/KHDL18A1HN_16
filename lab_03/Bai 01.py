n = int(input("Nhap n: "))
S = 1
P = 1
for k in range(1, n + 1):
    P *= (2 * k) / (2 * k + 1)
    S += P
print("Gia tri cua bieu thuc:", round(S, 3))