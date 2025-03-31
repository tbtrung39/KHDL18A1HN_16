
import math
x = float(input("Nhập giá trị x: "))
sai_so = 1e-4
so_hang = 1  
cos_x = so_hang  
n = 2  
while abs(so_hang) > sai_so:
    so_hang *= (-1) * x * x / ((n - 1) * n)  
    cos_x += so_hang
    n += 2  
print(f"Giá trị gần đúng của cos({x}) là: {cos_x}")
