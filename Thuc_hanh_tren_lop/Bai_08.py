xA = float(input("Nhập tọa độ x của điểm A: "))
yA = float(input("Nhập tọa độ y của điểm A: "))
xB = float(input("Nhập tọa độ x của điểm B: "))
yB = float(input("Nhập tọa độ y của điểm B: "))
xC = float(input("Nhập tọa độ x của điểm C: "))
yC = float(input("Nhập tọa độ y của điểm C: "))

trong_tam_x = round((xA + xB + xC) / 3, 2)
trong_tam_y = round((yA + yB + yC) / 3, 2)

print("Tọa độ trọng tâm tam giác là: (", trong_tam_x, ",", trong_tam_y, ")")