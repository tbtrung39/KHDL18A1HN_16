xA, yA = map(float, input("Nhập tọa độ A (xA, yA): ").split())
xB, yB = map(float, input("Nhập tọa độ B (xB, yB): ").split())
xC, yC = map(float, input("Nhập tọa độ C (xC, yC): ").split())
Gx = (xA + xB + xC) / 3
Gy = (yA + yB + yC) / 3
Gx = round(Gx, 2)
Gy = round(Gy, 2)
print(f"Tọa độ trọng tâm G là: ({Gx}, {Gy})")