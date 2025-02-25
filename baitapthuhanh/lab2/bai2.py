import math
a, b, c = map(float, input("Nhập a, b, c: ").split())
delta = b**2 - 4*a*c
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"Nghiệm x1 = {x1}, x2 = {x2}")
elif delta == 0:
    x = -b / (2*a)
    print(f"Nghiệm kép x = {x}")
else:
    print("Phương trình vô nghiệm.")