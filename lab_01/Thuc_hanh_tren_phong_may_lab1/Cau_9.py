# Nhập tọa độ của điểm trong không gian Oxyz
x = float(input("Nhập tọa độ x: "))
y = float(input("Nhập tọa độ y: "))
z = float(input("Nhập tọa độ z: "))

# Tính tọa độ của điểm đối xứng qua các mặt phẳng
# Đối xứng qua mặt phẳng Oxy
x_oxy = x
y_oxy = y
z_oxy = -z

# Đối xứng qua mặt phẳng Oxz
x_oxz = x
y_oxz = -y
z_oxz = z

# Đối xứng qua mặt phẳng Oyz
x_oyz = -x
y_oyz = y
z_oyz = z

# In kết quả
print(f"Tọa độ điểm đối xứng qua mặt phẳng Oxy: ({round(x_oxy, 2)}, {round(y_oxy, 2)}, {round(z_oxy, 2)})")
print(f"Tọa độ điểm đối xứng qua mặt phẳng Oxz: ({round(x_oxz, 2)}, {round(y_oxz, 2)}, {round(z_oxz, 2)})")
print(f"Tọa độ điểm đối xứng qua mặt phẳng Oyz: ({round(x_oyz, 2)}, {round(y_oyz, 2)}, {round(z_oyz, 2)})")