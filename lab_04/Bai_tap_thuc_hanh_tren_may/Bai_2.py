# a. S = 1/1 - 1/2 + 1/3 - 1/4 + 1/5 - …
S = 0
i = 1
sign = 1  # Dấu của từng số hạng
n = 10000  # Số lượng số hạng tính tổng

while i <= n:
    S += sign * (1 / i)
    sign = -sign  # Đảo dấu
    i += 1

print("Tổng a:", S)

# b. S = 1/2 + 1/(2*3) + 1/(3*4) + 1/(4*5) + …
S = 0
i = 2
n = 10000  # Số lượng số hạng tính tổng

while i <= n:
    S += 1 / (i * (i + 1))
    i += 1

print("Tổng b:", S)

# c. S = 1/sqrt(2) + 1/sqrt(3) + 1/sqrt(4) + 1/sqrt(5) + …
S = 0
i = 2
n = 10000  # Số lượng số hạng tính tổng

while i <= n:
    S += 1 / (i ** 0.5)  # sqrt(i) = i ** 0.5
    i += 1

print("Tổng c:", S)