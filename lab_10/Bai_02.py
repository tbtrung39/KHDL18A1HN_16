#Bước 2(Bài 2):
import my_square

a = float(input("Nhập cạnh hình vuông: "))

chu_vi = my_square.ChuviHinhvuong(a)
dien_tich = my_square.Dien_tich_hinh_vuong(a)

print("Chu vi hình vuông:", chu_vi)
print("Diện tích hình vuông:", dien_tich)