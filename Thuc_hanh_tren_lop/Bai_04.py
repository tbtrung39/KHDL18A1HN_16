import math
#Nhập giá trị xx
x=float(input("Nhập giá trị x:"))

tu_so=-x+math.sqrt(x**2+4)
mau_so=math.sqrt(x**4+1)
f_x=tu_so/mau_so
f_x="{:.2f}".format(f_x)

#In kết quả
print("Giá trị của f(x) là:",f_x)