x = float(input("Nhập tọa độ x: ")) 
y = float(input("Nhập tọa độ y: ")) 
z = float(input("Nhập tọa độ z: ")) 
doi_x_Oxy = (x, y, -z) 
doi_x_Oxz = (x, -y, z) 
doi_x_Oyz = (-x, y, z) 
print("\nTọa độ điểm đối xứng:") 
print(f"Qua mặt phẳng Oxy: {doi_x_Oxy}") 
print(f"Qua mặt phẳng Oxz: {doi_x_Oxz}") 
print(f"Qua mặt phẳng Oyz: {doi_x_Oyz}")