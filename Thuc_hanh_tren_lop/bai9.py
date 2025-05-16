import datetime

def main():
    try:
        ngay = int(input("Nhập ngày: "))
        thang = int(input("Nhập tháng: "))
        nam = int(input("Nhập năm: "))

        date = datetime.date(nam, thang, ngay)
        week_number = date.isocalendar()[1]
        print(f"Ngày {date.strftime('%d/%m/%Y')} thuộc tuần thứ {week_number} trong năm.")

    except ValueError:
        print("Lỗi: Ngày không hợp lệ!")

main()