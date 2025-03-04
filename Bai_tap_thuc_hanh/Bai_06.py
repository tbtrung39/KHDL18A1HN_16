U = 220 
I = 2.7
t = int(input("Nhập thời gian sử dụng (giây): "))
gia_dien = 7000
P = U * I 
E = (P * t) / 3600000
tien_dien = E * gia_dien
print("Tiền điện phải trả là:", tien_dien, "đồng")