a = float(input("Nhập giá trị của a: "))
b = float(input("Nhập giá trị của b: "))
c = float(input("Nhập giá trị của c: "))
x_dinh = -b / (2 * a)
y_dinh = a * x_dinh ** 2 + b * x_dinh + c
print("Tọa độ đỉnh của phương trình bậc 2 là:", (round(x_dinh, 2), round(y_dinh, 2)))