
n = int(input("Nhập số hàng n: "))
print("Tam giác (c):")
for i in range(1, n + 1):
    print(" " * (n - i), end=" ")
    print("*" * (2 * i - 1))
