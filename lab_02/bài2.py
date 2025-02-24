import math
a = float(input("Nhap he so a: "))
b = float(input("Nhap he so b: "))
c = float(input("Nhap he so c: "))
if a == 0:
    if b == 0:
        if c == 0:
            print("Phuong trinh co vo so nghiem.")
        else:
            print("Phuong trinh vo nghiem.")
    else:
        x = -c / b
        print(f"Phuong trinh co mot nghiem: x = {x}")
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phuong trinh vo nghiem.")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Phuong trinh co nghiem kep: x = {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Phuong trinh co hai nghiem phan biet: x1 = {x1}, x2 = {x2}")