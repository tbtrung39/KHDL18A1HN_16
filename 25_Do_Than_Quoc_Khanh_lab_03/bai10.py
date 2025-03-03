n = int(input("Nhập số nguyên dương: "))

while n <= 1:
    n = int(input("Nhập lại số nguyên dương (n > 1): "))

print("Phân tích thừa số nguyên tố của", n, "là:", end=" ")

i = 2
while n > 1:
    while n % i == 0:
        print(i, end=" ")
        n //= i
    i += 1
