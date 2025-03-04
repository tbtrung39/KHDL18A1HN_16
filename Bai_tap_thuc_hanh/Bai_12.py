import math   
a = float(input("Nhập vận tốc a (m/s): "))  
thoi_gian = round(-math.log(a / 5) / 4, 2)  
print(f"Thời gian để xe dừng lại là: {thoi_gian} giây")