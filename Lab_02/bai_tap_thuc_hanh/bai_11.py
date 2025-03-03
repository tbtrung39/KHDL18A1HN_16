ngay = int(input("Nhập vào ngày: "))
thang = int(input("Nhập vào tháng: "))

so_ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if thang < 1 or thang > 12 or ngay < 1 or ngay > so_ngay_trong_thang[thang - 1]:
    print("Ngày hoặc tháng không hợp lệ")
else:
    if ngay == so_ngay_trong_thang[thang - 1]:
        ngay = 1
        thang += 1
        if thang == 13:
            thang = 1
    else:
        ngay += 1

    print(f"Ngày tiếp theo là: {ngay}/{thang}")