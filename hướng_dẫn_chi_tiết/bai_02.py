a,b = map(float,input('Nhập tọa độ tâm I: ').split())
r = float(input('Mời nhập bán kính R: '))
x,y = map(float,input('Nhập tọa độ điểm M: ').split())
#Khoảng cách từ điểm I tới điểm M
import math
d = math.sqrt((x-a)**2 + (y-b)**2)
if d<r: print('Điểm M nằm trong đường tròn')
elif d==r: print('Điểm M nằm trên đuòngư tròn')
else:
    print('Điểm M nằm ngoài đường tròn')
    