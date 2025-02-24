num = int(input("Nhập số nguyên có ba chữ số: "))

if num < 100 or num > 999:
    print("Số không hợp lệ!")
else:
    hundreds = num // 100
    tens = (num // 10) % 10
    ones = num % 10

    # Đọc hàng trăm
    if hundreds == 1:
        print("Một trăm", end=" ")
    elif hundreds == 2:
        print("Hai trăm", end=" ")
    elif hundreds == 3:
        print("Ba trăm", end=" ")
    elif hundreds == 4:
        print("Bốn trăm", end=" ")
    elif hundreds == 5:
        print("Năm trăm", end=" ")
    elif hundreds == 6:
        print("Sáu trăm", end=" ")
    elif hundreds == 7:
        print("Bảy trăm", end=" ")
    elif hundreds == 8:
        print("Tám trăm", end=" ")
    elif hundreds == 9:
        print("Chín trăm", end=" ")

    # Đọc hàng chục
    if tens == 0:
        if ones != 0:
            print("lẻ", end=" ")
    elif tens == 1:
        print("mười", end=" ")
    elif tens == 2:
        print("hai mươi", end=" ")
    elif tens == 3:
        print("ba mươi", end=" ")
    elif tens == 4:
        print("bốn mươi", end=" ")
    elif tens == 5:
        print("năm mươi", end=" ")
    elif tens == 6:
        print("sáu mươi", end=" ")
    elif tens == 7:
        print("bảy mươi", end=" ")
    elif tens == 8:
        print("tám mươi", end=" ")
    elif tens == 9:
        print("chín mươi", end=" ")

    # Đọc hàng đơn vị
    if ones == 1:
        if tens >= 2:
            print("mốt")
        else:
            print("một")
    elif ones == 2:
        print("hai")
    elif ones == 3:
        print("ba")
    elif ones == 4:
        print("bốn")
    elif ones == 5:
        if tens == 0:
            print("năm")
        else:
            print("lăm")
    elif ones == 6:
        print("sáu")
    elif ones == 7:
        print("bảy")
    elif ones == 8:
        print("tám")
    elif ones == 9:
        print("chín")
