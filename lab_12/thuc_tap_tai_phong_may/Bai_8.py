import datetime

def tim_ngay_truoc():
    try:
        # Nhập dữ liệu từ người dùng
        ngay = int(input("Nhập ngày: "))
        thang = int(input("Nhập tháng: "))
        nam = int(input("Nhập năm: "))

        # Tạo đối tượng ngày
        ngay_hien_tai = datetime.date(nam, thang, ngay)

        # Tính ngày trước đó
        ngay_truoc = ngay_hien_tai - datetime.timedelta(days=1)

        print("Ngày trước đó là:", ngay_truoc.strftime("%d/%m/%Y"))

    except ValueError:
        print("Lỗi: Ngày không hợp lệ.")

# Gọi hàm
tim_ngay_truoc()