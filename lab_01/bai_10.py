import math
x = float(input("Nhập giá trị x: "))
log_x_4 = math.log(x, 4)
log_x_2 = math.log(x, 2)
fx = log_x_4 + log_x_2
fx = round(fx, 6)
print(f"{fx}")
