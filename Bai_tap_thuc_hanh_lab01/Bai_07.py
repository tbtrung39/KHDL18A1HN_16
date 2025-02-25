a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("NHập hệ số c: "))
x_dinh = -b/2*a
y_dinh = a*(x_dinh**2) + b*(x_dinh) + c
print(f"Đỉnh của phương trình bậc 2 là: ({x_dinh:.2f}, {y_dinh:.2f})")
