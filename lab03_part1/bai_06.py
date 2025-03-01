n = int(input("Nhập n: "))
S = 0
for i in range(1, n + 1):
    S += i ** 3  # Lũy thừa bậc 3
print("Tổng bậc 3 của", n, "số nguyên đầu tiên là:", S)
