import math
a = float(input("Nhap he so a: "))
b = float(input("Nhap he so b: "))
c = float(input("Nhap he so c: "))
delta = b**2 - 4*a*c
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"Nghiem cua phuong trinh: x1 = {x1:.2f}, x2 = {x2:.2f}")
elif delta == 0:
    x = -b / (2*a)
    print(f"Phuong trinh co nghiem kep: x = {x:.2f}")
else:
    print("Phuong trinh vo nghiem")