thang = int(input("Nhập tháng:"))
nam = int(input("Nhập năm:"))
if thang in [1,3,5,7,8,10,12]:
    ngay=31
elif thang in [4,6,9,11]:
    ngay=30
elif thang == 2 and (nam%4==0 and nam%100!=0) or nam %400==0:
    ngay = 29
else:
    ngay = 28
print("Tháng ",thang,"có ",ngay,"ngày")
