import datetime
try:
    ngay = int(input("Nhập ngày: "))
    thang = int(input("Nhập tháng: "))
    nam = int(input("Nhập năm: "))
    d = datetime.date(nam, thang, ngay)
    ngay_ke_tiep = d + datetime.timedelta(days=1)
    print("Ngày kế tiếp là:", ngay_ke_tiep.strftime("%d/%m/%Y"))
except ValueError:
    print("Lỗi: Ngày không hợp lệ. Vui lòng kiểm tra lại.")