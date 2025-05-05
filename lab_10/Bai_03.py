#Bước 2(Bài 3):
import sohoc

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
n = int(input("Nhập số n: "))

print("Ước chung lớn nhất của a và b là:", sohoc.Ucln(a, b))
print("Bội chung nhỏ nhất của a và b là:", sohoc.Bcnn(a, b))
print("Tổng các ước của n là:", sohoc.SumDivisor(n))