r = float(input('Nhập số đo bán kính R :'))
h = float(input('Nhập số đo chiều cao H :'))
sxq = 2*3.14*r*h
stp = 2*3.14*r*(r+h)
vkt = 3.14*r**2*h
print('Diện tích xung quanh là :',sxq)
print('Diện tích toàn phần là :',stp)
print('Thể tích khối trụ là :',vkt) 
