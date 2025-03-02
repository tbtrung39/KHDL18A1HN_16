n = int(input("Nhập n: "))
sum = 0
i = 1

while i <= n:
    term = (2 * i + 1) / (2 * i + 3)
    sum += term
    i += 1

print("Kết quả:", round(sum, 3))
