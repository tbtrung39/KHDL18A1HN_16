x, y, z = map(float, input("Nhập tọa độ điểm M: ").split())
print(f"Điểm đối xứng qua Oxy: ({x}, {y}, {-z})")
print(f"Điểm đối xứng qua Oxz: ({x}, {-y}, {z})")
print(f"Điểm đối xứng qua Oyz: ({-x}, {y}, {z})")