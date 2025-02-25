import math
x = float(input("Nhập giá trị x: "))
log_x = math.log(x)
log_2 = math.log(2)
log_4 = math.log(4)
f = (log_x / log_4) + (log_2 / log_x)
print(f"Giá trị của f(x) là: {f:.2f}")