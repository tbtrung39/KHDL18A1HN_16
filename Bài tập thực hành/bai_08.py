a1,a2=map(float,input('Nhập tọa độ  đỉnh A:').split())
b1,b2=map(float,input('Nhập tọa độ  đỉnh B:').split())
c1,c2=map(float,input('Nhập tọa độ  đỉnh C:').split())
G1=a1+b1+c1/3
G2=a2+b2+c2/3
print(f'Trọng tâm G của tam giác là:({G1},{G2})')