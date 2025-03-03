n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập lại n (n > 0): "))

sum = 0.0
i = 1

while i <= n:
    sum += 1 / i
    i += 1

print("Tổng nghịch đảo:", round(sum, 3))
