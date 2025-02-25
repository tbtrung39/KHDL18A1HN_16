x1, y1 = map(float, input("Nhập tọa độ điểm A (x1, y1): ").split())
x2, y2 = map(float, input("Nhập tọa độ điểm B (x2, y2): ").split())
x3, y3 = map(float, input("Nhập tọa độ điểm C (x3, y3): ").split())
xG = (x1 + x2 + x3) / 3
yG = (y1 + y2 + y3) / 3
xG_rounded = round(xG, 2)
yG_rounded = round(yG, 2)
print(f"Tọa độ trọng tâm G của tam giác là: ({xG_rounded}, {yG_rounded})")
