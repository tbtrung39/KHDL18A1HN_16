t=int(input('Nhập thời gian sử dụng (giây):'))
U=220
I=2.7
P=U*I#Tính công suất tiêu thụ(W)
H=t/3600#đổi giây sang giờ
E=P*H#Tính điện năng tiêu thụ(kWh)
gia_tien_dien=7000
tien_dien=E*gia_tien_dien
print('Tiền điẹn phải trả là:%tien_dien')
