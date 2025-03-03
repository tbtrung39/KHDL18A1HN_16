n = int(input("Nhap so hang: "))
# a)
print("\n(a)")
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
# b)
print("\n(b)")
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        if i == 0 or i == n - 1 or j == 0 or j == 2 * i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
# c)
print("\n(c)")
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()