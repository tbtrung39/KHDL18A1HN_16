import math
x = float(input("Nhap x: "))
log4_x = math.log(x) / math.log(4)
logx_2 = math.log(2) / math.log(x)
f_x = log4_x + logx_2
print("Gia tri cua bieu thuc f(x) la:", round(f_x, 2))