month = int(input("Nhập tháng (1-12): "))
months_name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
if 1 <= month <= 12:
    print(f"Tháng {month} là {months_name[month - 1]}.")
else:
    print("Tháng không hợp lệ.")