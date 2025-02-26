n = int(input("Nhập số hàng của tam giác: "))

#a
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)


# bb
for i in range(1, n + 1):
    if i == 1 or i == n:
        print(" " * (n - i) + "* " * i)
    else:
        print(" " * (n - i) + "*" + " " * (2 * (i - 1) - 1) + "*")

print()  

#cc
for i in range(1, n + 1):
    if i == n:
        print("* " * n)
    elif i == 1:
        print(" " * (n - i) + "*")
    else:
        print(" " * (n - i) + "*" + " " * (2 * (i - 1) - 1) + "*")

