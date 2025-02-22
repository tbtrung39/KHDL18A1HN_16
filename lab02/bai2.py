a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a == 0:
    if b == 0:
        print("Phương trình vô nghiệm" if c != 0 else "Phương trình có vô số nghiệm")
    else:
        print("Phương trình có một nghiệm:", -c / b)
else:
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        print("Phương trình có hai nghiệm:", x1, "và", x2)
    elif delta == 0:
        print("Phương trình có nghiệm kép:", -b / (2*a))
    else:
        print("Phương trình vô nghiệm")
