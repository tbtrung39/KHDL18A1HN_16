x = float(input("Nhập tọa độ x: "))
y = float(input("Nhập tọa độ y: "))
z = float(input("Nhập tọa độ z: "))

# Tính toán điểm đối xứng
oxy_x = x
oxy_y = y
oxy_z = -z

oxz_x = x
oxz_y = -y
oxz_z = z

oyz_x = -x
oyz_y = y
oyz_z = z

# Xuất kết quả
print("Điểm đối xứng qua mặt phẳng Oxy: (", oxy_x, ",", oxy_y, ",", oxy_z, ")")
print("Điểm đối xứng qua mặt phẳng Oxz: (", oxz_x, ",", oxz_y, ",", oxz_z, ")")
print("Điểm đối xứng qua mặt phẳng Oyz: (", oyz_x, ",", oyz_y, ",", oyz_z, ")")
