import math
x = float(input("Nhập giá trị x: ").split())
tu_so = -x + math.sqrt(x**2 + 4)
mau_so = 7 * math.sqrt(x**4 + 1)
f_x = tu_so / mau_so
print(f"Giá trị của biểu thức là: {f_x}")
