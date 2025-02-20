a = float(input("Nhập giá trị a: ")) 
b = float(input("Nhập giá trị b: ")) 
c = float(input("Nhập giá trị c: ")) 
dinh_x = -b / (2 * a) 
dinh_y = a * dinh_x**2 + b * dinh_x + c 
dinh_x = round(dinh_x , 2) 
dinh_y = round(dinh_y , 2)
print(f"Đỉnh của phương trình bậc 2 là: ({dinh_x}, {dinh_y})")