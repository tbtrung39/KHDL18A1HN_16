x_a, y_a = map(float, input("Nhap toa do diem A (x y): ").split())
x_b, y_b = map(float, input("Nhap toa do diem B (x y): ").split())
x_c, y_c = map(float, input("Nhap toa do diem C (x y): ").split())
x_g = (x_a + x_b + x_c) / 3
y_g = (y_a + y_b + y_c) / 3
print(f"Toa do trong tam G: ({x_g:.2f}, {y_g:.2f})")