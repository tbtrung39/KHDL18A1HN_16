while True:
    day = int(input("Nhập số thứ trong tuần (1 -> 7): "))
    if day == 1:
        print("Ngày bạn nhập là: Sunday")
        break
    elif day == 2:
        print("Ngày bạn nhập là: Monday")
        break
    elif day == 3:
        print("Ngày bạn nhập là: Tuesday")
        break
    elif day == 4:
        print("Ngày bạn nhập là: Wednesday")
        break
    elif day == 5:
        print("Ngày bạn nhập là: Thursday")
        break
    elif day == 6:
        print("Ngày bạn nhập là: Friday")
        break
    elif day == 7:
        print("Ngày bạn nhập là: Saturday")
        break
    else:
        print("Số nhập không hợp lệ. Vui lòng nhập lại.")
