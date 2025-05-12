import my_Triange
a=int(input("Nhap vao so do canh a: "))
b=int(input("Nhap vao so do canh b: "))
c=int(input("Nhap vao so do canh c: "))

if my_Triange.is_TamGiac(a, b, c):
    print("Ba canh tao thanh mot tam giac.")
    print("Chu vi tam giac la:", my_Triange.ChuviTamGiac(a, b, c))
    print("Dien tich tam giac la:", my_Triange.S_TamGiac(a, b, c))
else:
    print("Ba canh khong tao thanh mot tam giac.")