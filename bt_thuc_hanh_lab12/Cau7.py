import datetime

try:
    ngay = int(input("Nhập ngày: "))
    thang = int(input("Nhập tháng: "))
    nam = int(input("Nhập năm: "))

    d = datetime.datetime(nam, thang, ngay)
    d_ke_tiep = d + datetime.timedelta(days=1)

    print("Ngày kế tiếp là:", d_ke_tiep.strftime("%d-%m-%Y"))

except ValueError:
    print("Lỗi: Ngày không hợp lệ!")