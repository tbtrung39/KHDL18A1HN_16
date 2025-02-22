kw=int(input("Nhap so dien tieu thu: "))
if kw>0 and kw<=100:
    print("Tien dien phai nop: ",kw*2000)
elif kw>=101 and kw<=200:
    print("Tien dien phai nop: ",kw*2500)
elif kw>=201 and kw<=300:
    print("Tien dien phai nop: ",kw*3000)
elif kw>300:
    print("Tien dien phai nop: ",kw*5000)
else:
    print("Khong hop le, vui long nhap lai")