import datetime
try:
    day = int(input("Nhập ngày: "))
    month = int(input("Nhập tháng: "))
    year = int(input("Nhập năm: "))
    hn = datetime.date(year, month, day)
    ht = hn - datetime.timedelta(days=1)

    print("Ngày trước đó là:", ht.strftime("%d/%m/%Y"))

except ValueError:
    print("Lỗi")