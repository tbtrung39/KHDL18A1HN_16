x = float(input("Nhap toa do x cua diem P: "))
y = float(input("Nhap toa do y cua diem P: "))
z = float(input("Nhap toa do z cua diem P: "))
dx_oxy = (x, y, -z)
dx_oxz = (x, -y, z)
dx_oyz = (-x, y, z)
print(f"Diem doi xung qua mat phang Oxy: {dx_oxy}")
print(f"Diem doi xung qua mat phang Oxz: {dx_oxz}")
print(f"Diem doi xung qua mat phang Oyz: {dx_oyz}")