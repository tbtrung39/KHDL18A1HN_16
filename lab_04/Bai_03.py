import math
x = float(input("Nhập giá trị x (radian): "))
cos_x = 1  
so_hang = 1   
n = 1     
while abs(so_hang) > 10**-4:
    so_hang = ((-1)**n * x**(2*n)) / math.factorial(2*n)
    cos_x += so_hang
    n += 1
print("Giá trị gần đúng của cos(",x,") là:", cos_x)