# Câu 6. Tính tiền điện tiêu thụ của bóng đèn
U = 220  
I = 2.7  
gia_dien = 7000  
t = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))
P = U * I  
E = P * (t / 3600) / 1000  
tien_dien = E * gia_dien
tien_dien = int(tien_dien * 100) / 100  
print("Số tiền điện phải trả:", tien_dien, "VND")