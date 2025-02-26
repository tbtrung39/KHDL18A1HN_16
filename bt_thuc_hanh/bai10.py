n = int(input("Nhập số nguyên dương: "))
for _ in range(n):
    if n > 0:
        break
    n = int(input("Vui lòng nhập số nguyên dương: "))

print("Phân tích thừa số nguyên tố của", n, ":", end=" ")
i = 2
for i in range(2, n + 1):
    while n % i == 0:
        print(i, end=" ")
        n //= i
print()
