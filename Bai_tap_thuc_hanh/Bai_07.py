from datetime import datetime, timedelta

try:
    d = int(input("Ngày: "))
    m = int(input("Tháng: "))
    y = int(input("Năm: "))
    date = datetime(y, m, d)
    next_day = date + timedelta(days=1)
    print("Ngày kế tiếp:", next_day.strftime("%d-%m-%Y"))
except Exception as e:
    print("Lỗi:", e)
