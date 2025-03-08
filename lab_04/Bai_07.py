
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
while b != 0:
    a, b = b, a % b
ucln = a
bcnn = abs(a * b) // ucln
print("Bội chung nhỏ nhất là:", bcnn)