# 9

def tim_diem_doi_xung(x, y, z):
    print(f"Điểm đối xứng qua mặt phẳng Oxy: ({x}, {y}, {-z})")
    print(f"Điểm đối xứng qua mặt phẳng Oxz: ({x}, {-y}, {z})")
    print(f"Điểm đối xứng qua mặt phẳng Oyz: ({-x}, {y}, {z})")

# Nhập dữ liệu từ bàn phím
x = float(input("Nhập tọa độ x: "))
y = float(input("Nhập tọa độ y: "))
z = float(input("Nhập tọa độ z: "))

# Gọi hàm mà không cần return
tim_diem_doi_xung(x, y, z)