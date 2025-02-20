xA, yA = map(float, input("Nhập tọa độ điểm A (xA yA): ").split())
xB, yB = map(float, input("Nhập tọa độ điểm B (xB yB): ").split())
xC, yC = map(float, input("Nhập tọa độ điểm C (xC yC): ").split())
xG = (xA + xB + xC) / 3
yG = (yA + yB + yC) / 3
print(f"Tọa độ trọng tâm G: ({xG:.2f}, {yG:.2f})")
