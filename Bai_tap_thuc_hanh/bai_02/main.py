import my_square

a = float(input("Nhập cạnh hình vuông: "))

chu_vi = my_square.ChuviHinhvuong(a)
dien_tich = my_square.Dien_tich_hinh_vuong(a)

print(f"Chu vi hình vuông là: {chu_vi}")
print(f"Diện tích hình vuông là: {dien_tich}")
