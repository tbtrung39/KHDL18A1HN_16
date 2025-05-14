import math

try:
    a = float(input("Nhap canh a: "))
    b = float(input("Nhap canh b: "))
    c = float(input("Nhap canh c: "))
    
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Canh tam giac phai la so duong lon hon 0.")

    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Ba canh khong thoa man dieu kien ton tai cua tam giac.")

    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("Dien tich tam giac la:", s)

except ValueError as v:
    print("Loi:", v)

except Exception as e:
    print("Loi:", e)