print('chuong trinh kiem tra 1 thang co bao nhieu ngay')
print('nhap thang can kiem tra:',end='')
thang=int(input())
if thang==2:
    print("thang", thang,  "co 29 ngay")
elif thang==1 or thang==3 or thang==5 or thang==7 or thang==8 or thang==10 or thang==12:
    print("thang",thang,"co 31 ngay")
elif thang==4 or thang==6 or thang==9 or thang==11:
    print("thang", thang , "co 30 ngay")
else:
    print("thang khong hop le, vui long nhap lai!")
    