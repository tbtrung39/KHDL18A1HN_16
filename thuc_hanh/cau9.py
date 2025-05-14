
import datetime

try:
    ngay = int(input("Nhập ngày: "))
    thang = int(input("Nhập tháng: "))
    nam = int(input("Nhập năm: "))

    d = datetime.datetime(nam, thang, ngay)
    tuan = d.isocalendar()[1]

    print(f"Ngày {d.strftime('%d-%m-%Y')} thuộc tuần thứ {tuan} của năm.")

except ValueError:
    print("Lỗi: Ngày không hợp lệ!")
