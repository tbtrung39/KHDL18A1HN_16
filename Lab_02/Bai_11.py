ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))

so_ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if 1 <= thang <= 12 and 1 <= ngay <= so_ngay_trong_thang[thang - 1]:
    if ngay < so_ngay_trong_thang[thang - 1]:
        ngay += 1
    elif ngay == so_ngay_trong_thang[thang - 1]:
        ngay = 1
        if thang < 12:
            thang += 1
        else:
            thang = 1
    print("Ngày tiếp theo là:", ngay, "/", thang)
else:
    print("Ngày hoặc tháng không hợp lệ!")