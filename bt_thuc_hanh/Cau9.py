# Câu 9
x = float(input("Nhap toa do x: "))
y = float(input("Nhap toa do y: "))
z = float(input("Nhap toa do z: "))

doi_xung_oxy = (x, y, -z)
doi_xung_oxz = (x, -y, z)
doi_xung_oyz = (-x, y, z)

print("Toa do doi xung qua mat phang Oxy:", doi_xung_oxy)
print("Toa do doi xung qua mat phang Oxz:", doi_xung_oxz)
print("Toa do doi xung qua mat phang Oyz:", doi_xung_oyz)
