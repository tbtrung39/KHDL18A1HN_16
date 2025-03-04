x_A = float(input("Nhập tọa độ x của đỉnh A: "))
y_A = float(input("Nhập tọa độ y của đỉnh A: "))
x_B = float(input("Nhập tọa độ x của đỉnh B: "))
y_B = float(input("Nhập tọa độ y của đỉnh B: "))
x_C = float(input("Nhập tọa độ x của đỉnh C: "))
y_C = float(input("Nhập tọa độ y của đỉnh C: "))
x_G = (x_A + x_B + x_C) / 3
y_G = (y_A + y_B + y_C) / 3
print("Tọa độ trọng tâm của tam giác là: ({:.2f}, {:.2f})".format(x_G, y_G))