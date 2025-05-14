import my_Triange
a, b, c = map(float,input("Nhập độ dài 3 cạnh tam giác: ").split())
if my_Triange.is_TamGiac(a,b,c):
    print(f"Chu vi tam giác là: {my_Triange.ChucviTamGiac(a,b,c):.2f}")
    print(f"Diện tích tam giác là: {my_Triange.S_TamGiac(a,b,c):.2f}")
else:
    print("Đây không phải tam giác!!!!!")
