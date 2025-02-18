r=float(input("Nhap so do ban kinh cua khoi tru: "))
h=float(input("Nhap chieu cao cua khoi tru: "))
s_xq=2*3.14*r*h
s_tp= s_xq + 2*3.14*r*r
v=3.14*r*r*h
print(f"Dien tich xung quanh: {s_xq:.2f}")
print(f"Dien tich toan phan: {s_tp:.2f}")
print(f"The tich: {v:.2f}")
