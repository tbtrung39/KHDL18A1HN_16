n = int(input("Nhập số nguyên n: "))
total = 0
for i in range(1, n + 1):
    total += i ** 3  
print("Tổng bậc 3 của", n, "số nguyên đầu tiên là:", total)
