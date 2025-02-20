print('chương trình cho phép nhập số KW điện tiêu thụ và tính tiền điện:') 
so_Kw=float(input('Nhập số Kw:')) 
if 0 <= so_Kw <=100: 
    print('đơn giá 2000 đồng/KW.') 
elif 101<= so_Kw <= 200: 
     print('đơn giá 2500 đồng/KW5') 
elif 201<= so_Kw <= 300: 
     print('đơn giá 3000 đồng/KW') 
else: 
     print('đơn giá 5000 đồng/KW.') 

 