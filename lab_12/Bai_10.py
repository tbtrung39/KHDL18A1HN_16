from datetime import datetime
def tinh_khoang_cach(date1, date2):
    if date1 > date2:
        date1, date2 = date2, date1
    nam1, thang1, ngay1 = date1.year, date1.month, date1.day
    nam2, thang2, ngay2 = date2.year, date2.month, date2.day
    nam = nam2 - nam1
    thang = thang2 - thang1
    ngay = ngay2 - ngay1
    if ngay < 0:
        thang -= 1
        from calendar import monthrange
        thang_truoc = thang2 - 1 if thang2 > 1 else 12
        nam_truoc = nam2 if thang2 > 1 else nam2 - 1
        ngay += monthrange(nam_truoc, thang_truoc)[1]
    if thang < 0:
        thang += 12
        nam -= 1
    return nam, thang, ngay
try:
    s1 = input("Nhập ngày thứ nhất (dd-mm-yyyy): ")
    s2 = input("Nhập ngày thứ hai (dd-mm-yyyy): ")
    d1 = datetime.strptime(s1, "%d-%m-%Y").date()
    d2 = datetime.strptime(s2, "%d-%m-%Y").date()
    nam, thang, ngay = tinh_khoang_cach(d1, d2)
    print(f"Hai ngày cách nhau: {nam} năm, {thang} tháng, {ngay} ngày.")
except ValueError:
    print("Lỗi: Vui lòng nhập đúng định dạng dd-mm-yyyy.")