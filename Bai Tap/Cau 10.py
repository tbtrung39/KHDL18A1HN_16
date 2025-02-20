import math   
x = float(input("Nhập vào giá trị x: "))   
log4_x = math.log(x, 4) 
log_x_2 = math.log(2, x)  
f_x = log4_x + log_x_2  
f_x = round(f_x, 2)    
print("Giá trị của f(x) là:", f_x)