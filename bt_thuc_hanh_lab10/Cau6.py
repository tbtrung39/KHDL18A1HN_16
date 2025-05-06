# Cau 6
def ucln(x,y):
    while y != 0:
        x, y = y, x % y
    return x

def bcnn(x,y):

    return (x * y)/ucln(x,y)
x = int(input("Nhập x: "))
y = int(input("Nhập y: " ))
print(bcnn(x,y))