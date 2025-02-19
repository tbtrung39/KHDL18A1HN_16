x = float(input("Nhập tọa độ x: "))
y = float(input("Nhập tọa độ y: "))
z = float(input("Nhập tọa độ z: "))
x_Oxy = x
y_Oxy = y
z_Oxy = -z
x_Oxz = x
y_Oxz = -y
z_Oxz = z
x_Oyz = -x
y_Oyz = y
z_Oyz = z
print(f"Tọa độ điểm đối xứng qua mặt phẳng Oxy là: ({x_Oxy}, {y_Oxy}, {z_Oxy})")
print(f"Tọa độ điểm đối xứng qua mặt phẳng Oxz là: ({x_Oxz}, {y_Oxz}, {z_Oxz})")
print(f"Tọa độ điểm đối xứng qua mặt phẳng Oyz là: ({x_Oyz}, {y_Oyz}, {z_Oyz})")
