x1, y1 = map(float, input("Nhập tọa độ A(x1,y1): ").split())
x2, y2 = map(float, input("Nhập tọa độ B(x2,y2): ").split())
x3, y3 = map(float, input("Nhập tọa độ C(x3,y3): ").split())
g1= (x1 + x2 + x3) / 3
g2= (y1 + y2 + y3) / 3
print(f"Tọa độ trọng tâm của tam giác là: ({g1:.2f}, {g2:.2f})")