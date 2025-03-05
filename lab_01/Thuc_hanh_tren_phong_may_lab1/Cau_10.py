import math

# Nhập giá trị x
x = float(input("Nhập giá trị của x: "))

# Kiểm tra x có hợp lệ không (x > 0)
if x <= 0:
    print("Giá trị x không hợp lệ. x phải lớn hơn 0.")
else:
    # Tính log cơ số 4 của x
    log4_x = math.log(x) / math.log(4)

    # Tính log cơ số x của 2
    logx_2 = math.log(2)

    # Tính giá trị của biểu thức
    f_x = log4_x + logx_2

    # Làm tròn đến hai chữ số thập phân
    f_x = round(f_x, 2)

    # In kết quả
    print("Giá trị của f(x) là:", f_x)