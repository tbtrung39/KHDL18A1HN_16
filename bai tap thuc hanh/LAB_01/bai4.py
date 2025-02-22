x = float(input("Nhập giá trị x: "))
f_x = (-x + (x**2 + 4) * (1/2)) / ((x**4 + 1) * (1/7))
f_x = round(f_x, 2)
print("Giá trị của biểu thức f(x) là:", f_x)