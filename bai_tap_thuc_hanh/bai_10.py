from hinhhoc import my_Triange, my_square

a, b, c = 3, 4, 5
if my_Triange.is_TamGiac(a, b, c):
    print("Ba cạnh tạo thành một tam giác.")
    print("Chu vi tam giác:", my_Triange.ChuviTamGiac(a, b, c))
    print("Diện tích tam giác:", my_Triange.S_TamGiac(a, b, c))
else:
    print("Ba cạnh không tạo thành một tam giác.")
canh = 5
print("\nHình vuông:")
print("Chu vi hình vuông:", my_square.ChuviHinhVuong(a))
print("Diện tích hình vuông:", my_square.DientichHinhVuong(a))