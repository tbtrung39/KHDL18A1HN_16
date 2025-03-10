a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))

x = a
y = b
while y != 0:
    temp = y
    y = x % y
    x = temp

ucln = x  

bcnn = (a * b) // ucln

print("Bội chung nhỏ nhất của", a, "và", b, "là:", bcnn)
