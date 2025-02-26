n = int(input("Nhập n: "))
for _ in range(n):
    if n > 0:
        break
    n = int(input("Vui lòng nhập n dương: "))

S = 0
for i in range(1, n + 1):
    S += 1 / i
print("Tổng S:", S)
