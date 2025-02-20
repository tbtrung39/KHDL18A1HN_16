# Câu 3
r = float(input("Ban kinh: "))
h = float(input("Chieu cao: "))

pi = 3.14

dt_xq = round(2 * pi * r * h, 2)
dt_tp = round(2 * pi * r * (r + h), 2)
the_tich = round(pi * r**2 * h, 2)

print("Dien tich xung quanh:", dt_xq)
print("Dien tich toan phan:", dt_tp)
print("The tich:", the_tich)
