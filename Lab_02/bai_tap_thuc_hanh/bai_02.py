import math

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a == 0:
    if b == 0:
        ket_qua = "Phương trình vô nghiệm"
    else:
        ket_qua = f"Phương trình có một nghiệm: x = {-c/b}"
else:
    delta = b*b - 4*a*c
    if delta < 0:
        ket_qua = "Phương trình vô nghiệm"
    elif delta == 0:
        ket_qua = f"Phương trình có nghiệm kép: x = {-b/(2*a)}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        ket_qua = f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}"

print(ket_qua)