thang = int(input("Nhap thang(1-12):"))
if thang<1 or thang>12:
    print("Khong hop le vui long nhap lai")
else:
    print("Nhap vao nam can kiem tra:", end='')
    nam = int(input())
    if thang ==2:
        if (nam % 4 ==0 and nam % 100 !=0) or (nam % 400 ==0):
            print ("Thang", thang, "co 29 ngay")
        else: 
            print("Thang", thang, " co 28 ngay")
    elif thang in [1,3,5,7,8,10,12]:
        print("Thang", thang, "co 31 ngay")
    else:
        print("Thang",thang,"co 30 ngay")

