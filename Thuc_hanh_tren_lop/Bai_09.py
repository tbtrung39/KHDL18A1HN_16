# Nhập tọa độ x, y, z
x = float(input("Nhập tọa độ x: "))
y = float(input("Nhập tọa độ y: "))
z = float(input("Nhập tọa độ z: "))

# In kết quả
print(f"Tọa độ đối xứng qua mặt phẳng Oxy: ({x}, {-y}, {z})")
print(f"Tọa độ đối xứng qua mặt phẳng Oxz: ({x}, {y}, {-z})")
print(f"Tọa độ đối xứng qua mặt phẳng Oyz: ({-x}, {y}, {z})")