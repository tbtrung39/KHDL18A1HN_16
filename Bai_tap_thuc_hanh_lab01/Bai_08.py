print("Tọa độ đỉnh A")
a, b = map(float,input("Nhập tọa độ đỉnh A: ").split())
print("Tọa độ đỉnh B")
a1, b1= map(float,input("Nhập tọa độ đỉnh B: ").split())
print("Tọa độ đỉnh C")
a2, b2= map(float,input("Nhập tọa độ đỉnh C:").split())
Gx = (a + a1 + a2)/3
Gy = (b + b1+ b2)/3
print(f"Trọng tâm cua tam giác ABC: ({Gx:.2f},{Gy:.2f})")
