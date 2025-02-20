thang=int(input("Nhap vao mot thang:"))
if thang in [1,3,5,7,8,10,12]:
    print("Thang", thang,"co 31 ngay")
elif thang in [4,6,9,11]:
    print("Thang", thang,"co 30 ngay")
elif thang==2:
    print("Thang 2 co 28 ngay hoac 29 ngay(nam nhuan).")
else:
    print("Thang khong hop le.")