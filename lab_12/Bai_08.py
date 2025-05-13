import datetime
try:
    ngay = int(input("Nhập ngày: "))
    thang = int(input("Nhập tháng: "))
    nam = int(input("Nhập năm: "))
    d = datetime.date(nam, thang, ngay)
    ngay_truoc = d - datetime.timedelta(days=1)
    print("Ngày trước đó là:", ngay_truoc.strftime("%d/%m/%Y"))
except ValueError:
    print("Lỗi: Ngày không hợp lệ. Vui lòng kiểm tra lại.")