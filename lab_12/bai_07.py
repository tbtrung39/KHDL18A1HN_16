import datetime

try:
    day = int(input("Nhập ngày: "))
    month = int(input("Nhập tháng: "))
    year = int(input("Nhập năm: "))
    hn = datetime.date(year, month, day)
    hs = hn + datetime.timedelta(days=1)
    
    print("Ngày kế tiếp là:", hs.strftime("%d/%m/%Y"))
except ValueError:
    print("Loi")