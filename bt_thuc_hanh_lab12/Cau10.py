import datetime

def tinh_khoang_cach(date1, date2):
    delta = abs((date2 - date1).days)
    nam = delta // 365
    thang = (delta % 365) // 30
    ngay = (delta % 365) % 30
    return nam, thang, ngay

try:
    s1 = input("Nhập ngày thứ nhất (dd-mm-yyyy): ")
    s2 = input("Nhập ngày thứ hai (dd-mm-yyyy): ")

    d1 = datetime.datetime.strptime(s1, "%d-%m-%Y")
    d2 = datetime.datetime.strptime(s2, "%d-%m-%Y")

    nam, thang, ngay = tinh_khoang_cach(d1, d2)
    print(f"Hai ngày cách nhau {nam} năm, {thang} tháng, {ngay} ngày.")

except ValueError:
    print("Lỗi: Định dạng ngày không hợp lệ!")