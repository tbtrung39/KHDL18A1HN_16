tk=float(input("Nhap diem tong ket cua hoc sinh: "))
if tk<0.0 or tk>10.0:
    print("Khong hop le, vui long nhap lai")
elif tk>=0 and tk<=3:
    print("Kem")
elif tk==4:
    print("Yeu")
elif tk>=5 and tk<=6:
    print("Trung binh")
elif tk>=7 and tk<=8:
    print("Kha")
else:
    print("Gioi")