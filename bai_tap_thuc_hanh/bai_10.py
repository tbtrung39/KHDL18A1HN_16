from datetime import datetime
from dateutil.relativedelta import relativedelta 

try:
    d1 = input("Nhập ngày thứ nhất (dd-mm-yyyy): ")
    d2 = input("Nhập ngày thứ hai (dd-mm-yyyy): ")

    date1 = datetime.strptime(d1, "%d-%m-%Y")
    date2 = datetime.strptime(d2, "%d-%m-%Y")

    if date1 > date2:
        date1, date2 = date2, date1

    diff = relativedelta(date2, date1)
    print(f"Khoảng cách: {diff.years} năm, {diff.months} tháng, {diff.days} ngày")

except ValueError:
    print("Ngày không hợp lệ!")
