def ucln(x,y):
    while y != 0:
        x, y = y, x % y
    return x
x = int(input("Nhập x: "))
y = int(input("Nhập y: " ))
print(ucln(x,y)) 