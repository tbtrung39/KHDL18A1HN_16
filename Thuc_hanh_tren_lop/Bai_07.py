# Nhập giá trị a, b, c
a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
c = float(input("Nhập giá trị c: "))

# Tọa độ đỉnh x
x_đỉnh = -b / (2 * a)

# Tọa độ đỉnh y
y_đỉnh = (4 * a * c - b * b) / (4 * a)

# In kết quả
print(f"Tọa độ đỉnh của phương trình là: ({x_đỉnh:.2f},
{y_đỉnh:.2f})")