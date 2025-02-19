import math
r = float(input("Nhập bán kính: "))
h = float(input("Nhập chiều cao: "))
Sxq =  2*math.pi*r*h
Stp = (2*math.pi*r*h) + (2*math.pi*r*r)
print(f"Diện tích xung quanh là: {Sxq:.2f}")
print(f"Diện tích toàn phần là: {Stp:.2f}")