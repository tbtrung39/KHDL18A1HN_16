print('Chương trình kiểm tra số ngày của một tháng:') 
print('Nhập tháng cần kiểm tra (1-12):', end='') 
thang = int(input()) 
if thang in [1, 3, 5, 7, 8, 10, 12]: 
    print(f"Tháng {thang} có 31 ngày") 
elif thang in [4, 6, 9, 11]: 
    print(f"Tháng {thang} có 30 ngày") 
elif thang == 2: 
    print("Tháng 2 có 28 hoặc 29 ngày (tùy vào năm nhuận)") 
else: 
    print("Tháng không hợp lệ! ") 