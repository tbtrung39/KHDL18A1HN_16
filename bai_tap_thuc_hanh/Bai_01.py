import math

def kiem_tra_tam_giac():
    try:
        a = float(input("nhập chiều dài cạnh a: "))
        b = float(input("nhập chiều dài cạnh b: "))
        c = float(input("nhập chiều dài cạnh c: "))
        if  a <= 0 or b<= 0 or c <= 0:
                raise ValueError("các cạnh tam giác phải lớn hơn 0")
        if (a + b <= c) or (a + c <= b) or (b+c <= a):
                raise ValueError("ba cạnh không đủ đièu kiện tạo thành tam giác")
        nua_cv = (a+ b+ c)/2
        dt = math.sqrt(nua_cv*(nua_cv-a)*(nua_cv-b)*(nua_cv-c))       
        print("diện tích tam giác là:", dt)
    except ValueError as loi:
        if "could not convert" in str(loi):
           print("lỗi:vui lòng nhập lại giá trị số")
        else:
             print("lỗi: ",loi)
kiem_tra_tam_giac()
                
