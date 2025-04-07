n = int(input("Nhap so sinh vien: "))
d = {}
for i in range(n):
    ma = input("Nhap ma sinh vien (6 so): ")
    ten = input("Nhap ten sinh vien: ")
    diem = int(input("Nhap diem (0-10): "))
    d[ma] = (ten, diem)
sinh_vien_sap_xep = sorted(d.items(), key=lambda x: x[1][1], reverse=True)
for ma, (ten, diem) in sinh_vien_sap_xep:
    print(ma, ten, diem)