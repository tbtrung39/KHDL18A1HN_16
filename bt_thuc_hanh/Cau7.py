# Câu 7
a = float(input("Gia tri a: "))
b = float(input("Gia tri b: "))
c = float(input("Gia tri c: "))

x_dinh = round(-b / (2 * a), 2)
y_dinh = round(a * x_dinh**2 + b * x_dinh + c, 2)

print("Toa do dinh cua phuong trinh bac 2 la (x, y):", x_dinh, y_dinh)
