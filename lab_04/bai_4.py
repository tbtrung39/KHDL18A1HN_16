
t=int(input("Nhap vao tu so: "))
m=int(input("Nhap vao mau so: "))
while m==0:
    print("Mau so khong hop le, vui long nhap lai!")
    m=int(input("Nhap vao mau so: "))
print(f"Phan so ban vua nhap la: {t}/{m}")
