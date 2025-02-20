ten = {1: "Sunday", 
       2: "Monday", 
       3: "Tuesday", 
       4: "Wednesday", 
       5: "Thursday", 
       6: "Friday", 
       7: "Saturday" 
} 
thu = int(input('Nhập số thứ trong tuần(1-7):')) 
if 1<= thu <=7: 
    print(f'Thứ {thu} : {ten[thu]}') 
else: 
    print("Không hợp lệ vui lòng nhập lại") 