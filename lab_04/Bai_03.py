import math

x = float(input("Nhập x: "))

x = x % (2 * math.pi)
if x > math.pi:
    x -= 2 * math.pi

cos_x = 1
term = 1  
n = 1 
while abs(term) > 1e-4:
    term *= (-1) * x * x / ((2 * n - 1) * (2 * n))  
    cos_x += term
    n += 1

print("Giá trị gần đúng của cos(x):", cos_x)