a,b = map(float,input("nhập tọa độ tâm I: "))
r = float(input("nhập bán kính R: "))
x,y = map(float,input("nhập tọa độ điểm M: "))
import math
d = math.sqrt((x-a)**2 + (y-b)**2)
if d<r: print("điểm M nằm trong đường tròn")
elif d==r: print("điểm M nằm trên đường tròn")
else : print("điểm M nằm ngoài đường tròn") 