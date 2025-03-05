# Nhập các hệ số a, b, c của phương trình bậc 2
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Tính tọa độ đỉnh của phương trình bậc 2
x_dinh = -b / (2 * a)
y_dinh = -(b**2 - 4 * a * c) / (4 * a)

# In kết quả làm tròn đến 2 chữ số thập phân
print(f"Tọa độ đỉnh của phương trình bậc 2 là: ({round(x_dinh, 2)}, {round(y_dinh, 2)})")