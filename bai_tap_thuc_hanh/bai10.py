from datetime import datetime

try:
    ngay1s = input("Nhập ngày thứ nhất (dd-mm-yyyy): ")
    ngay2s = input("Nhập ngày thứ hai (dd-mm-yyyy): ")

    ngay1 = datetime.strptime(ngay1s, "%d-%m-%Y")
    ngay2 = datetime.strptime(ngay2s, "%d-%m-%Y")

    if ngay1 > ngay2:
        ngay1, ngay2 = ngay2, ngay1

    chenh_lech = (ngay2 - ngay1).days

    nam = chenh_lech // 365
    con_lai = chenh_lech % 365
    thang = con_lai // 30
    ngay = con_lai % 30

    print(f"Hai ngày cách nhau khoảng {nam} năm, {thang} tháng, {ngay} ngày.")

except ValueError:
    print("Lỗi")