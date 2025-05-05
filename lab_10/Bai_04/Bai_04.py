#Bước 2(Bài 4 ):
import giaipt

print("Giải phương trình bậc nhất ax + b = 0")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
print(giaipt.pt_bac_nhat(a, b))

print("\nGiải phương trình bậc hai ax^2 + bx + c = 0")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
print(giaipt.pt_bac_hai(a, b, c))