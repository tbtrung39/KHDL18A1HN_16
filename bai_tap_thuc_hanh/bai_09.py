from datetime import datetime

days = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"]

try:
    date_str = input("Nhập ngày (dd-mm-yyyy): ")
    date_obj = datetime.strptime(date_str, "%d-%m-%Y")
    day_of_week = date_obj.weekday()
    print("Ngày đó là:", days[day_of_week])
except ValueError:
    print("Ngày không hợp lệ!")