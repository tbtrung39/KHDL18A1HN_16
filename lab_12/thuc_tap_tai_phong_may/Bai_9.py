import datetime

def tim_tuan_thu_may():
    try:
        # Nhập ngày tháng năm từ người dùng
        ngay = int(input("Nhập ngày: "))
        thang = int(input("Nhập tháng: "))
        nam = int(input("Nhập năm: "))

        # Tạo đối tượng ngày
        ngay_nhap = datetime.date(nam, thang, ngay)

        # Dùng hàm isocalendar() để lấy số tuần ISO (tuần bắt đầu từ thứ 2)
        # Kết quả trả về: (năm, số tuần, thứ trong tuần)
        iso_calendar = ngay_nhap.isocalendar()
        so_tuan = iso_calendar[1]

        print(f"Ngày {ngay_nhap.strftime('%d/%m/%Y')} thuộc tuần thứ {so_tuan} trong năm {nam}.")

    except ValueError:
        print("Lỗi: Ngày không hợp lệ.")

# Gọi hàm
tim_tuan_thu_may()