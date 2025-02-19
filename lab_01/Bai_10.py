
x = float(input("Nhap gia tri cua x: "))
if x > 0:  
    f_x = (3 / 2) * (x ** 0.5)  
    f_x = round(f_x, 2)  
    print("Gia tri cua bieu thuc f(x) la:", f_x)
else:
    print("Khong hop le vui long nhap lai")