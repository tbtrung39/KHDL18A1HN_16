n=int(input("Nhập số hàng của tam giác:"))
i = 1
while i <= n:
    j = 1
    while j <= n - i:
        print(" ", end="")
        j += 1
    j = 1
    while j <= 2 * i - 1:
        if j == 1 or j == 2 * i - 1 or i == n:
            print("*", end="")
        else:
            print(" ", end="")
        j += 1
    print()
    i += 1

print()  
