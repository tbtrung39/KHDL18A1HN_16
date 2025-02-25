x = float(input("Nhập giá trị x: "))
if x <= 0:
    print("Giá trị x phải lớn hơn 0.")
else:
    log4_x = (x ** 0.5) / (4 ** 0.5) 
    log_x_2 = (2 ** 0.5) / (x ** 0.5)  
    f_x = log4_x + log_x_2
    f_x_rounded = round(f_x, 2)
    print(f"Giá trị của f(x) là: {f_x_rounded}")
