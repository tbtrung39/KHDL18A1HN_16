a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
c = float(input("Nhập giá trị c: "))
if a != 0:
 dinh_x = -b / (2 * a)
 dinh_y = c - (b**2) / (4 * a)
 dinh_x = round(dinh_x, 2)
 dinh_y = round(dinh_y, 2)
 print(f"Tọa độ đỉnh của phương trình bậc hai là: ({dinh_x},
{dinh_y})")
else:
 print("Giá trị a phải khác 0 để là phương trình bậc hai.")