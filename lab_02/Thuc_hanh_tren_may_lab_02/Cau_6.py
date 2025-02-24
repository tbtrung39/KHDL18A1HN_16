# Nhập số nguyên có 3 chữ số
so = int(input("Nhập vào một số nguyên có ba chữ số: "))

# Kiểm tra số có đúng 3 chữ số không
if so < 100 and so > -100:
    print("Số không hợp lệ! Vui lòng nhập số có ba chữ số.")
else:
    # Xử lý dấu âm
    if so < 0:
        print("Âm", end=" ")
        so = abs(so)  # Lấy giá trị tuyệt đối để dễ xử lý

    # Lấy từng chữ số hàng trăm, chục, đơn vị
    hang_tram = so // 100
    hang_chuc = (so // 10) % 10
    hang_dv = so % 10

    # Đọc hàng trăm
    if hang_tram == 1:
        print("Một trăm", end=" ")
    elif hang_tram == 2:
        print("Hai trăm", end=" ")
    elif hang_tram == 3:
        print("Ba trăm", end=" ")
    elif hang_tram == 4:
        print("Bốn trăm", end=" ")
    elif hang_tram == 5:
        print("Năm trăm", end=" ")
    elif hang_tram == 6:
        print("Sáu trăm", end=" ")
    elif hang_tram == 7:
        print("Bảy trăm", end=" ")
    elif hang_tram == 8:
        print("Tám trăm", end=" ")
    elif hang_tram == 9:
        print("Chín trăm", end=" ")

    # Xử lý đọc hàng chục và hàng đơn vị
    if hang_chuc == 0:
        if hang_dv != 0:
            print("lẻ", end=" ")
    elif hang_chuc == 1:
        if hang_dv == 0:
            print("mười", end=" ")
        elif hang_dv == 5:
            print("mười lăm", end=" ")
        else:
            print("mười", end=" ")
    elif hang_chuc == 2:
        if hang_dv == 0:
            print("hai mươi", end=" ")
        elif hang_dv == 5:
            print("hai mươi lăm", end=" ")
        else:
            print("hai mươi", end=" ")
    elif hang_chuc == 3:
        print("ba mươi", end=" ")
    elif hang_chuc == 4:
        print("bốn mươi", end=" ")
    elif hang_chuc == 5:
        print("năm mươi", end=" ")
    elif hang_chuc == 6:
        print("sáu mươi", end=" ")
    elif hang_chuc == 7:
        print("bảy mươi", end=" ")
    elif hang_chuc == 8:
        print("tám mươi", end=" ")
    elif hang_chuc == 9:
        print("chín mươi", end=" ")

    # Đọc hàng đơn vị
    if hang_chuc != 1:
        if hang_dv == 1:
            print("một")
        elif hang_dv == 2:
            print("hai")
        elif hang_dv == 3:
            print("ba")
        elif hang_dv == 4:
            print("bốn")
        elif hang_dv == 5 and hang_chuc != 0:
            print("lăm")
        elif hang_dv == 5:
            print("năm")
        elif hang_dv == 6:
            print("sáu")
        elif hang_dv == 7:
            print("bảy")
        elif hang_dv == 8:
            print("tám")
        elif hang_dv == 9:
            print("chín")