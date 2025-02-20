import math
a = float(input("Nhập vào hệ số a: "))
b = float(input("Nhập vào hệ số b: "))
c = float(input("Nhập vào hệ số c: "))
delta = b**2 - 4*a*c
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình có vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        nghiem = -c / b
        print(f"Phương trình có nghiệm duy nhất: x = {nghiem}")
else:
    if delta < 0:
        print("Phương trình vô nghiệm.")
    elif delta == 0:
        nghiem_kep = -b / (2*a)
        print(f"Phương trình có nghiệm kép: x = {nghiem_kep}")
    else:
        nghiem_1 = (-b + math.sqrt(delta)) / (2*a)
        nghiem_2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Phương trình có hai nghiệm phân biệt: x1 = {nghiem_1}, x2 = {nghiem_2}")
