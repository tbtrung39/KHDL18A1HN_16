# Bài 7: Tìm đỉnh của phương trình bậc 2
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
x_dinh = -b / (2 * a)
y_dinh = (- (b ** 2 - 4 * a * c)) / (4 * a)
print("Tọa độ đỉnh của phương trình bậc 2:", (round(x_dinh, 2), round(y_dinh, 2)))
