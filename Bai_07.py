a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
x = a
y = b
while y != 0:
    x, y = y, x % y
ucln = x
bcnn = abs(a*b)//ucln
print(bcnn)