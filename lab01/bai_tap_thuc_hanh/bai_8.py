a, b = map(float,input("Nhập tọa độ A: ").split())
a1, b1 = map(float,input("Nhập tọa độ B: ").split())
a2, b2 = map(float,input("Nhập tọa độ C: ").split())
Gx = (a + a1+ a2)/3
Gy = (b + b1 + b2 )/3
print(f"Trọng tâm của tam giác là: ({Gx},{Gy})")