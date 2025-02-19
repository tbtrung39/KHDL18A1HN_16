import math
x = float(input("Nhập giá trị x: ").split())
log4_x = math.log(x) / math.log(4)  # log4(x) = log(x) / log(4)
logx_2 = math.log(2) / math.log(x)  # logx(2) = log(2) / log(x)
f_x = log4_x + logx_2
print(f"Giá trị của biểu thức là: {f_x}")
