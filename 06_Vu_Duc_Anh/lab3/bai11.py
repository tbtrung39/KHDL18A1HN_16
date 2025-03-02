n = int(input("Nhập số dòng: "))
i = 1

while i <= n:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1

n = int(input("Nhập số dòng: "))
i = n

while i >= 1:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i -= 1

n = int(input("Nhập số dòng: "))
i = 1

while i <= n:
    j = 1
    while j <= n - i:
        print(" ", end=" ")
        j += 1
    j = 1
    while j <= 2 * i - 1:
        print("*", end=" ")
        j += 1
    print()
    i += 1
