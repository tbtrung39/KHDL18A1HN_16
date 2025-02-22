# Bài 9: Tìm trọng tâm tam giác
x1 = float(input("Nhập tọa độ x của điểm A: "))
y1 = float(input("Nhập tọa độ y của điểm A: "))
x2 = float(input("Nhập tọa độ x của điểm B: "))
y2 = float(input("Nhập tọa độ y của điểm B: "))
x3 = float(input("Nhập tọa độ x của điểm C: "))
y3 = float(input("Nhập tọa độ y của điểm C: "))
x_trong_tam = (x1 + x2 + x3) / 3
y_trong_tam = (y1 + y2 + y3) / 3
print("Tọa độ trọng tâm tam giác:", (round(x_trong_tam, 2), round(y_trong_tam, 2)))
