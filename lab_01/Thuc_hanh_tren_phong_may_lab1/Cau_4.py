import math

# Nhập giá trị x
x = float(input("Nhập giá trị của x: "))

# Tính giá trị của biểu thức bậc 7
phan_tu_1 = -x
phan_tu_2 = math.sqrt(x**2 + 4)
phan_tu_3 = math.sqrt(x**4 + 1)
f_x = phan_tu_1 + phan_tu_2 / phan_tu_3

# Làm tròn đến hai chữ số thập phân
f_x = round(f_x, 2)

# In kết quả
print("Giá trị của f(x) là:", f_x)