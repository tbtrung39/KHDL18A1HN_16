
x = float(input("Nhập giá trị x: "))
tu_so = -x + (x**2 + 4)**(1/2)  
mau_so = (x**4 + 1)**(1/7)      
f_x = tu_so / mau_so
print("Giá trị của biểu thức f(x) là:", round(f_x, 2))