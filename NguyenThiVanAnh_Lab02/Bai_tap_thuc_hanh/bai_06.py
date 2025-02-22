n=int(input("Nhap vao mot so nguyen co ba chu so:"))
if (n>=100 and n<=999) or (n<=-100 and n>=-999):
    if n<0:
        print("Âm",end=" ")
    tram=n//100
    chuc=(n//10)%10
    dv=n%10
    if tram==1:
        print("một trăm",end=" ")
    elif tram==2:
        print("hai trăm",end=" ")
    elif tram==3:
        print("ba trăm",end=" ")
    elif tram==4:
        print("bốn trăm",end=" ")
    elif tram==5:
        print("năm trăm",end=" ")
    elif tram==6:
        print("sáu trăm",end=" ")
    elif tram==7:
        print("bảy trăm",end=" ")
    elif tram==8:
        print("tám trăm",end=" ")
    elif tram==9:
        print("chín trăm",end=" ")
    if chuc==0 and dv==0:
        print()
    elif chuc==0 and dv!=0:
        print("lẻ",end=" ")
    elif chuc==1:
        print("mười",end=" ")
    elif chuc==2:
        print("hai mươi",end=" ")
    elif chuc==3:
        print("ba mươi",end=" ")
    elif chuc==4:
        print("bốn mươi",end=" ")
    elif chuc==5:
        print("năm mươi",end=" ")
    elif chuc==6:
        print("sáu mươi",end=" ")
    elif chuc==7:
        print("bảy mươi",end=" ")
    elif chuc==8:
        print("tám mươi",end=" ")
    elif chuc==9:
        print("chín mươi",end=" ")
    if dv==1 and chuc>1:
        print("mốt")
    elif dv==1 and chuc==0:
        print("một")
    elif dv==5 and chuc>0:
        print("lăm")
    elif dv==5 and chuc==0:
        print("năm")
    elif dv==2:
        print("hai")
    elif dv==3:
        print("ba")
    elif dv==4:
        print("bốn")
    elif dv==5:
        print("năm")
    elif dv==6:
        print("sáu")
    elif dv==7:
        print("bảy")
    elif dv==8:
        print("tám")
    elif dv==9:
        print("chín")
else:
        print("Số nhập vào không hợp lệ, vui lòng nhập lại số có ba chữ số")