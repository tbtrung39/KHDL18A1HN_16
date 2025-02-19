a = float(input("Nhập giá trị a: ").split())
b = float(input("Nhập giá trị b: ")).split()
c = float(input("Nhập giá trị c: ").split())
x_dinh = -b / (2 * a)
y_dinh = a * x_dinh**2 + b * x_dinh + c
print(f"Đỉnh của phương trình bậc hai là: ({x_dinh}, {y_dinh})")
