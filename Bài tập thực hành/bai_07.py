print('chương trình in ra học lực của học sinh theo thang điểm:') 
Diem_TK=float(input('Nhập điểm:')) 
if 0.0 <= Diem_TK <=3.0: 
    print('Loại Kém') 
elif Diem_TK == 4.0: 
     print('Loại yếu.25') 
elif 5.0<= Diem_TK <= 6.0: 
     print('Loại TB') 
elif 7.0 <= Diem_TK <= 8.0: 
     print('Loại Khá') 
elif 9.0 <= Diem_TK <= 10.0: 
     print('Loại Giỏi') 
else: 
     print('Điểm không hợp lệ') 