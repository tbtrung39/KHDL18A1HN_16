import math 
a, b, c=map(float,input("Xin moi nhap do dai 3 canh: ").split()) 
chuvi=a + b + c 
p=chuvi/2 
dientich=math.sqrt(p*(p-a)*(p-b)*(p-c)) 
print(f"Chu vi cua tam giac la {chuvi:.2f}") 
print(f"Dien tich cua tam giac la {dientich:.2f}") 