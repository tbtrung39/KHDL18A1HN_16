day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))

if month < 1 or month > 12 or day < 1:
    print("Ngày hoặc tháng không hợp lệ!")
else:
    if month == 2:
        max_day = 28
    elif month in (4, 6, 9, 11):
        max_day = 30
    else:
        max_day = 31

    if day > max_day:
        print("Ngày không hợp lệ!")
    else:
        if day < max_day:
            next_day = day + 1
            next_month = month
        else:
            next_day = 1
            next_month = month + 1 if month < 12 else 1

        print("Ngày tiếp theo là:", next_day, "/", next_month)
