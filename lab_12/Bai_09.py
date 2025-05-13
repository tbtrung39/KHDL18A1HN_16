import datetime
try:
    ngay = int(input("Nhập ngày: "))
    thang = int(input("Nhập tháng: "))
    nam = int(input("Nhập năm: "))
    d = datetime.date(nam, thang, ngay)
    _, so_tuan, _ = d.isocalendar()
    print(f"Ngày {d.strftime('%d/%m/%Y')} thuộc tuần thứ {so_tuan} trong năm.")
except ValueError:
    print("Lỗi: Ngày không hợp lệ. Vui lòng kiểm tra lại.")