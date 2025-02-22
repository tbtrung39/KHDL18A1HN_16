thang=int(input("Nhap thang: "))
if thang<1 or thang>12:
    print("Không hợp lệ, vui lòng nhập lại!")
else:
    print("Nhập vào năm cần kiểm tra: ",end="")
    nam=int(input())
    if thang==2:
        if(nam % 4 == 0 and nam % 100 !=0) or nam % 400 == 0:
            print("Tháng",thang,"có 29 ngày")
        else:
            print("Tháng",thang,"có 28 ngày")
    else:
        if thang==1 or thang==3 or thang==5 or thang==7 or thang==8 or thang==10 or thang==12:
            print("Tháng",thang,"có 31 ngày")
        else:
            print("Tháng",thang,"có 30 ngày")
