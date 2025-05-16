import datetime

def main():
    try:
        ngay = int(input("Nhập ngày: "))
        thang = int(input("Nhập tháng: "))
        nam = int(input("Nhập năm: "))

        today = datetime.date(nam, thang, ngay)
        tomorrow = today + datetime.timedelta(days=1)
        print("Ngày kế tiếp là:", tomorrow.strftime("%d/%m/%Y"))

    except ValueError:
        print("Lỗi: Ngày không hợp lệ!")

main()