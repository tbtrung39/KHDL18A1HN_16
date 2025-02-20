day = int(input("Nhập số ngày trong 1 tháng: "))
thang = int(input("Nhập tháng: "))
if thang == 1 or \
    thang == 3 or\
    thang == 5 or\
    thang == 7 or\
    thang == 8 or\
    thang == 10 or\
    thang == 12:
    if 1 <= day <= 31:
        day_new = day +1
        print(f"Ngày tiếp theo của ngày {day} tháng {thang} là: ngày {day_new} tháng {thang} ")
    else:
        print("Bạn nhập quá số ngày vui lòng nhập lại ngày")
elif thang == 4 or\
    thang == 6 or\
    thang == 9 or\
    thang == 11:
    if 1 <= day <= 30:
        day_new = day + 1
        print(f"Ngày tiếp theo của ngày {day} tháng {thang} là: ngày {day_new} tháng {thang}")
    else:
        print("Bạn nhập quá số ngày vui lòng nhập lại ngày")
elif thang == 2:
    if 1 <= day <= 28:
        day_new = day + 1
        print(f"Ngày tiếp theo của ngày {day} tháng {thang} là: ngày {day_new} tháng {thang}")
    else:
        print("Nhập quá số ngày vui lòng nhập lại")
else:
    print("Bạn nhập sai tháng vui lòng nhập lại")
