import datetime

def tim_ngay_ke_tiep():
    try:
        # Nhập dữ liệu từ người dùng
        ngay = int(input("Nhập ngày: "))
        thang = int(input("Nhập tháng: "))
        nam = int(input("Nhập năm: "))

        # Tạo đối tượng ngày
        ngay_hien_tai = datetime.date(nam, thang, ngay)

        # Tính ngày kế tiếp
        ngay_ke_tiep = ngay_hien_tai + datetime.timedelta(days=1)

        print("Ngày kế tiếp là:", ngay_ke_tiep.strftime("%d/%m/%Y"))

    except ValueError:
        print("Lỗi: Ngày không hợp lệ.")

# Gọi hàm
tim_ngay_ke_tiep()