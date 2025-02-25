xA, yA = map(float, input("Nhập tọa độ điểm A: ").split())
xB, yB = map(float, input("Nhập tọa độ điểm B: ").split())
xC, yC = map(float, input("Nhập tọa độ điểm C: ").split())
S = abs(xA*(yB - yC) + xB*(yC - yA) + xC*(yA - yB)) / 2
print(f"Diện tích tam giác: {S:.2f}")
