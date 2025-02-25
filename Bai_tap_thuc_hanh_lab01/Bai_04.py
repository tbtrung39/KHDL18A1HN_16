import math
x = float(input("Nhập x: "))
Fx = (-x + math.sqrt(x**2 + 4))/ (math.sqrt(x**4 +1))**1/7
print(f"Gía trị biểu thức là: {Fx:.2f}")