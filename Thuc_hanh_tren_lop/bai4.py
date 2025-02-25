x = float(input("Nhập giá trị x: "))
f_x = (-x + (x**2 + 4)**0.5) / ((x**4 + 1)**(1/7))
f_x_rounded = round(f_x, 2)
print(f"Giá trị của f(x) là: {f_x_rounded}")
