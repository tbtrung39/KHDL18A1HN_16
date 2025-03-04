import math
x = float(input("Nhập x (đơn vị radian): "))
term = 1  
cos_x = term  
n = 1 
while abs(term) >= 1e-4:  
    term *= -x**2 / ((2*n) * (2*n - 1))  
    cos_x += term  
    n += 1 
print(f"cos({x}) ≈ {cos_x}")
print(f"Giá trị thực tế: {math.cos(x)}") 
