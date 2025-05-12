from hinhhoc import ChuviHinhvuong, Dien_tich_hinh_vuong, ChuviTamGiac, DienTichTamGiac

# Hình vuông
a = float(input("Nhập cạnh hình vuông: "))
print("Chu vi hình vuông:", ChuviHinhvuong(a))
print("Diện tích hình vuông:", Dien_tich_hinh_vuong(a))

# Tam giác
a = float(input("Nhập cạnh a của tam giác: "))
b = float(input("Nhập cạnh b của tam giác: "))
c = float(input("Nhập cạnh c của tam giác: "))

if a + b > c and a + c > b and b + c > a:
    print("Chu vi tam giác:", ChuviTamGiac(a, b, c))
    print("Diện tích tam giác:", DienTichTamGiac(a, b, c))
else:
    print("Không phải là tam giác hợp lệ!")
