import math
x = float(input("Nhập giá trị x: "))
f_x = (math.log(x) / math.log(4)) + (math.log(2) / math.log(x))
f_x = round(f_x, 2)
print("Giá trị của biểu thức f(x) là:", f_x)