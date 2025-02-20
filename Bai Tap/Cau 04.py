import math  
x = float(input("Nhập giá trị của x: "))
f_x = (-x + math.sqrt(x**2 + 4)) / math.sqrt(7 * x**4 + 1) 
print(f"Giá trị của f({x}) là: {f_x:.2f}")
