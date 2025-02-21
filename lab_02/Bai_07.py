diem = float(input("Nhap diem:"))
if diem<0.0 or diem>10.0:
    print("Khong hop le vui long nhap lai")
elif diem>0 and diem<=3:
    print("Kem")
elif diem ==4 :
    print("Yeu")
elif diem >= 5 and diem<=6:
    print("Trung binh")
elif diem >=7 and diem<=8:
    print("Kha")
else:
    print("Gioi")