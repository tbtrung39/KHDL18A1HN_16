thu = int(input("Nhập vào thứ (1->7): "))
while thu not in range(1, 8):
    thu = int(input("Nhập lại thứ (1->7): "))

if thu == 1:
    ten_thu = "Sunday"
elif thu == 2:
    ten_thu = "Monday"
elif thu == 3:
    ten_thu = "Tuesday"
elif thu == 4:
    ten_thu = "Wednesday"
elif thu == 5:
    ten_thu = "Thursday"
elif thu == 6:
    ten_thu = "Friday"
elif thu == 7:
    ten_thu = "Saturday"
else:
    ten_thu = "Thứ không hợp lệ"

print(f"Thứ {thu} là {ten_thu}")
