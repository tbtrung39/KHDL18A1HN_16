days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
if thang < 1 or thang > 12 or ngay < 1 or ngay > days_in_month[thang - 1]:
    print("Ngày nhập không hợp lệ.")
else:
    ngay_tiep_theo = ngay + 1
    if ngay_tiep_theo > days_in_month[thang - 1]:
        ngay_tiep_theo = 1
        thang += 1
        if thang > 12:
            thang = 1
            nam += 1
    print("Ngày tiếp theo là:", ngay_tiep_theo, "/", thang, "/", nam)