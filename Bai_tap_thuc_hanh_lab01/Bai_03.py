import math
r = float(input("Nhập bán kính: "))
h = float(input("Nhập chiều cao: "))
Sxq = 2*math.pi*r*h
Stp = Sxq + 2*math.pi*r**2
print(round(Sxq))
print(round(Stp))
