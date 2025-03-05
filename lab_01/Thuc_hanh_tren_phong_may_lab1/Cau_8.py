# Nhập tọa độ 3 đỉnh A, B, C
xA = float(input("Nhập hoành độ điểm A: "))
yA = float(input("Nhập tung độ điểm A: "))
xB = float(input("Nhập hoành độ điểm B: "))
yB = float(input("Nhập tung độ điểm B: "))
xC = float(input("Nhập hoành độ điểm C: "))
yC = float(input("Nhập tung độ điểm C: "))

# Tính tọa độ trọng tâm G
xG = (xA + xB + xC) / 3
yG = (yA + yB + yC) / 3

# Làm tròn đến hai chữ số thập phân
xG = round(xG, 2)
yG = round(yG, 2)

# In kết quả
print(f"Tọa độ trọng tâm tam giác là: ({xG}, {yG})")