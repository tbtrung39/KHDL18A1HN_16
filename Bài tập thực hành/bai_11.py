ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
ngay = int(input("Nhập ngày: ")) 
thang = int(input("Nhập tháng: ")) 
if thang < 1 or thang > 12: 
    print("Tháng không hợp lệ.") 
elif ngay < 1 or ngay > ngay_trong_thang[thang - 1]: 
    print("Ngày không hợp lệ.") 
else: 
    ngay += 1 
    if ngay > ngay_trong_thang[thang - 1]: 
        ngay = 1   
        thang += 1 
        if thang > 12: 
            thang = 1  
    print(f"Ngày tiếp theo là: {ngay}/{thang}") 