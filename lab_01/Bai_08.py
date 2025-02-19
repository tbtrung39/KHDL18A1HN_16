
A_x = float(input("Nhập tọa độ A_x: "))
A_y = float(input("Nhập tọa độ A_y: "))
A_z = float(input("Nhập tọa độ A_z: "))
B_x = float(input("Nhập tọa độ B_x: "))
B_y = float(input("Nhập tọa độ B_y: "))
B_z = float(input("Nhập tọa độ B_z: "))
C_x = float(input("Nhập tọa độ C_x: "))
C_y = float(input("Nhập tọa độ C_y: "))
C_z = float(input("Nhập tọa độ C_z: "))
G_x = (A_x + B_x + C_x) / 3
G_y = (A_y + B_y + C_y) / 3
G_z = (A_z + B_z + C_z) / 3
G_x = round(G_x, 2)
G_y = round(G_y, 2)
G_z = round(G_z, 2)
print("Tọa độ trọng tâm G là:", (G_x, G_y, G_z))