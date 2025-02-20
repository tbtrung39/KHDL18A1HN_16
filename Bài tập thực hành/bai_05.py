ten = {1: "January", 
       2: "February", 
       3: "March", 
       4: "April", 
       5: "May", 
       6: "Jne", 
       7: "July", 
       8: "August", 
       9:"September", 
       10:"October", 
       11:"November", 
       12:"December", 
} 
thang = int(input('Nhập số tháng trong năm(1-12):')) 
if 1<= thang <=1212: 
    print(f'Tháng {thang} : {ten[thang]}') 
else: 
    print("Không hợp lệ vui lòng nhập lại") 

 