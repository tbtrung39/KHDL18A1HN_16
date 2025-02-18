import math
a = int(input('Vận tốc của oto đang chạy(km/h):'))
t=a**4/math.log(5,4)
print(f'Thời gian oto đi được cho đến lúc dừng là:%0.2f giờ'%t)