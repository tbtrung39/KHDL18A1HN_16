import giai_pt

print("1. Giải phương trình bậc nhất ax + b = 0")
a1 = float(input("Nhập a: "))
b1 = float(input("Nhập b: "))
print(giai_pt.giai_pt_bac_nhat(a1, b1))

print("\n2. Giải phương trình bậc hai ax^2 + bx + c = 0")
a2 = float(input("Nhập a: "))
b2 = float(input("Nhập b: "))
c2 = float(input("Nhập c: "))
print(giai_pt.giai_pt_bac_hai(a2, b2, c2))