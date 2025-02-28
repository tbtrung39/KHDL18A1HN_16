# Bài 10: Phân tích số nguyên thành tích thừa số nguyên tố
n = int(input("Nhập số nguyên dương: "))
i = 2
print("Dạng tích thừa số nguyên tố của", n, "là:", end=" ")
while n > 1:
    while n % i == 0:
        print(i, end=" ")
        n = n // i
    i = i + 1
print()