a, b, c = map(float, input("Nhập các hệ số a, b, c: ").split())
delta = b**2 - 4*a*c
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    print(f"Nghiệm kép: {-b / (2*a):.2f}")
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"Nghiệm x1 = {x1:.2f}, x2 = {x2:.2f}")