R = float(input("Nhập bán kính r: ")) 
h = float(input("Nhập chiều cao h: "))
S_xq = 2 * 3,14 * R * h 
S_tp = 2 * 3,14 * R * (R + h)
V = 3,14 * R * R * h
print('Diện tích xung quanh: ', S_xq) 
print('Diện tích toàn phần: ', S_tp) 
print('Thể tích: ', V)