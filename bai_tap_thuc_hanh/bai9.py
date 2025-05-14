import datetime
try:
    day = int(input("Nhập ngày: "))
    month = int(input("Nhập tháng: "))
    year = int(input("Nhập năm: "))

    date = datetime.date(year, month, day)
    week_number = date.isocalendar()[1]

    print(f"Ngày {date.strftime('%d/%m/%Y')} thuộc tuần thứ {week_number} của năm {year}")

except ValueError:
    print("Lỗi")