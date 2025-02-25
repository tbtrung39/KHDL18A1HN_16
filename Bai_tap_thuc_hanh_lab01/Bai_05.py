a, b, c = map(float,input("Nhập tọa độ cua vecto A: ").split())
x , y, z = map(float,input("Nhập tọa độ của vecto B: ").split())
tich_vo_huong = a*x + b*y + c*z
print(f"Tích vô hướng của AB là: {tich_vo_huong}")
