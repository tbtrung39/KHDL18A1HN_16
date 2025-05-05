
#Bước 2:(Bài 1)

import my_Triange 

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if my_Triange.is_TamGiac(a, b, c):
    print("Đây là một tam giác.")
    print("Chu vi tam giác:", my_Triange.ChuviTamGiac(a, b, c))
    print("Diện tích tam giác:", my_Triange.S_TamGiac(a, b, c))
else:
    print("Ba cạnh không tạo thành một tam giác.")