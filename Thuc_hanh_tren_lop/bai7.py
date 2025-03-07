a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
x = a
y = b
while b != 0:
    a, b = b, a % b
bcnn = abs(x * y) // a
print(f"Bội chung nhỏ nhất của {x} và {y} là: {bcnn}")
