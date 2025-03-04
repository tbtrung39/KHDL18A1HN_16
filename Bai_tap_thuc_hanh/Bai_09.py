x = float(input("Nhập tọa độ x: "))   
y = float(input("Nhập tọa độ y: "))   
z = float(input("Nhập tọa độ z: "))   
x_oxy = x   
y_oxy = y   
z_oxy = -z   
print(f"Đối xứng qua Oxy: ({x_oxy}, {y_oxy}, {z_oxy})")   
x_oxz = x   
y_oxz = -y   
z_oxz = z   
print(f"Đối xứng qua Oxz: ({x_oxz}, {y_oxz}, {z_oxz})")   
x_oyz = -x   
y_oyz = y   
z_oyz = z   
print(f"Đối xứng qua Oyz: ({x_oyz}, {y_oyz}, {z_oyz})")