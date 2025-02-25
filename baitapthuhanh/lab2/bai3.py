week_day = int(input("Nhập thứ (1-7): "))
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
if 1 <= week_day <= 7:
    print(f"Thứ {week_day} là {days[week_day - 1]}.")
else:
    print("Thứ không hợp lệ.")