ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))

if thang == 1:
    if ngay < 31:
        ngay = ngay + 1
    else:
        ngay = 1
        thang = 2
elif thang == 2:
    if ngay < 28:
        ngay = ngay + 1
    else:
        ngay = 1
        thang = 3
elif thang == 3:
    if ngay < 31:
        ngay = ngay + 1
    else:
        ngay = 1
        thang = 4
elif thang == 4:
    if ngay < 30:
        ngay = ngay + 1
    else:
        ngay = 1
        thang = 5
elif thang == 5:
    if ngay < 31:
        ngay = ngay + 1
    else:
        ngay = 1
        thang = 6
elif thang == 6:
    if ngay < 30:
        ngay = ngay + 1
    else:
        ngay = 1
        thang = 7
elif thang == 7:
    if ngay < 31:
        ngay = ngay + 1
    else:
        ngay = 1
        thang = 8
elif thang == 8:
    if ngay < 31:
        ngay = ngay + 1
    else:
        ngay = 1
        thang = 9
elif thang == 9:
    if ngay < 30:
        ngay = ngay + 1
    else:
        ngay = 1
        thang = 10
elif thang == 10:
    if ngay < 31:
        ngay = ngay + 1
    else:
        ngay = 1
        thang = 11
elif thang == 11:
    if ngay < 30:
        ngay = ngay + 1
    else:
        ngay = 1
        thang = 12
else:
    if ngay < 31:
        ngay = ngay + 1
    else:
        ngay = 1
        thang = 1

print(f"Ngày tiếp theo là: {ngay}/{thang}")