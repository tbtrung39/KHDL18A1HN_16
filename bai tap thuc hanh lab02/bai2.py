a = int(input('nhap he so a:'))
b = int(input('nhap he so b:'))
c = int(input('nhap he so c:'))
if a==0:
    print('phuong trinh vo nghiem.')
else:
    delta = b**2-4*a*c
    if delta < 0:
        print('phuong trinh vo nghiem')
    elif delta == 0:
        print('phuong trinh co nghiem kep', -b/2*a)
    elif delta > 0:
        print('phuong trinh co 2 nghiem phan biet:',"x1=", (-b+(delta)**1/2)/2*a, "x2=", (-b-(delta)**1/2)/2*a)
    else:
        print('khong hop le. vui long nhap lai')