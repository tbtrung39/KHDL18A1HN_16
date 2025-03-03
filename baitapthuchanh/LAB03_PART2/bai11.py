n = int(input('Nhập N: '))

#PHAN a
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    if i == 1:
        print("*")
    elif i == n:
        print("*" * (2 * i - 1))
    else:
        print("*" + " " * (2 * i - 3) + "*")

#PHAN b
for i in range(1, n + 1):
    if i == 1 or i == n:
        print(" " * (n - i) + "* " * i)
    else:
        print(" " * (n - i) + "* " + "  " * (i - 2) + "*")

#PHAN c
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)