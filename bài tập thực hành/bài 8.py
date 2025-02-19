xA = float(input("Nhập tọa độ xA: ").split())
yA = float(input("Nhập tọa độ yA: ").split())
xB = float(input("Nhập tọa độ xB: ").split())
yB = float(input("Nhập tọa độ yB: ").split())
xC = float(input("Nhập tọa độ xC: ").split())
yC = float(input("Nhập tọa độ yC: ").split())
xG = (xA + xB + xC) / 3
yG = (yA + yB + yC) / 3
print(f"Tọa độ trọng tâm của tam giác là: ({xG}, {yG})")
