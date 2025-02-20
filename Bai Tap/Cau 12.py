a = float(input("Nhập vào vận tốc a (m/s): "))  
t = float(input("Nhập vào thời gian t (giây): "))  
v_t = -t * math.log(5, 4) + a**4  
v_t = round(v_t, 2)  
print("Giá trị của v(t) là:", v_t)