a, b, c = map(float, input("Nhập hệ số a, b, c: ").split())
delta = b**2 - 4*a*c
x1 = (-b - delta**0.5) / (2*a)
x2 = (-b + delta**0.5) / (2*a)
x1 = round(x1, 6)
x2 = round(x2, 6)
print(f"{x1} {x2}")
