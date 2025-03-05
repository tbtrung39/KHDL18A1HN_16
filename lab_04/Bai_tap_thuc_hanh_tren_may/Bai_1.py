# Nhập n, đảm bảo n là số nguyên dương
n = 0
while n <= 0:
    print("Nhập số nguyên dương n:")
    n = int(input())
    if n <= 0:
        print("n phải lớn hơn 0, vui lòng nhập lại.")

# a) Tính S4 = 1^2 + 2^2 + ... + n^2
S4 = 0
i = 1
while i <= n:
    S4 += i ** 2
    i += 1

print("Tổng S4:", S4)

# b) Tính S5 = 1^3 + 3^3 + 5^3 + ... + (2n+1)^3
S5 = 0
i = 1
count = 0  # Đếm số số hạng đã tính

while count < n:
    S5 += i ** 3
    i += 2  # Chỉ xét số lẻ
    count += 1

print("Tổng S5:", S5)

# c) Tính S6 = 2^4 + 4^4 + 6^4 + ... + (2n)^4
S6 = 0
i = 2
count = 0  # Đếm số số hạng đã tính

while count < n:
    S6 += i ** 4
    i += 2  # Chỉ xét số chẵn
    count += 1

print("Tổng S6:", S6)