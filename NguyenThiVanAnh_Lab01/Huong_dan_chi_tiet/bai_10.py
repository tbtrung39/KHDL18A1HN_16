import math 
x,y=map(float,input("Nhap vao cac gia tri x,y: ").split()) 
f=math.sin(x)/((2*x+y)/math.cos(x))-x**y/(x-y) 
print("Gia tri cua bieu thuc la: %0.2f"%f)