from datetime import datetime

def tinh_khoang_cach_ngay():
    try:
        # Nhập ngày từ người dùng
        ngay1_str = input("Nhập ngày thứ nhất (dd-mm-yyyy): ")
        ngay2_str = input("Nhập ngày thứ hai (dd-mm-yyyy): ")

        # Chuyển đổi sang datetime object
        ngay1 = datetime.strptime(ngay1_str, "%d-%m-%Y")
        ngay2 = datetime.strptime(ngay2_str, "%d-%m-%Y")

        # Đảm bảo ngày1 < ngày2
        if ngay1 > ngay2:
            ngay1, ngay2 = ngay2, ngay1

        # Tính tổng số ngày chênh lệch
        delta_days = (ngay2 - ngay1).days

        # Tính năm, tháng, ngày tương đối (ước lượng)
        years = delta_days // 365
        months = (delta_days % 365) // 30
        days = (delta_days % 365) % 30

        print(f"Hai ngày cách nhau khoảng: {years} năm, {months} tháng, {days} ngày")

    except ValueError:
        print("Lỗi: Vui lòng nhập ngày đúng định dạng dd-mm-yyyy!")

# Gọi hàm
tinh_khoang_cach_ngay()