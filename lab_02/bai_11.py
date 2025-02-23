month = int(input("Nhập tháng (1-12): "))
day = int(input("Nhập ngày: "))
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    max_day = 31
elif month == 4 or month == 6 or month == 9 or month == 11:
    max_day = 30
elif month == 2:
    max_day = 28
else:
    max_day = 0 
if max_day == 0 or day < 1 or day > max_day:
    print("Ngày hoặc tháng không hợp lệ!")
else:
    next_day = day + 1
    next_month = month
    if next_day > max_day:
        next_day = 1
        next_month = month + 1
    if next_month > 12:
        next_month = 1    
    print("Ngày tiếp theo:", next_day, "/", next_month)