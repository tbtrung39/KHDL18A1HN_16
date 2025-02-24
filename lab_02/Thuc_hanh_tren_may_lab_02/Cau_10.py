# Nhập giờ bắt đầu và giờ kết thúc
gio_bat_dau = int(input("Nhập giờ bắt đầu (5 - 22): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc (5 - 22): "))

# Kiểm tra điều kiện hợp lệ
if gio_bat_dau < 5 or gio_ket_thuc > 22 or gio_bat_dau > gio_ket_thuc:
    print("Thời gian không hợp lệ! Vui lòng nhập lại.")
else:
    # Tính số giờ thuê sân
    so_gio_thue = gio_ket_thuc - gio_bat_dau

    # Đơn giá cơ bản
    don_gia_3h_dau = 100000
    don_gia_sau_3h = don_gia_3h_dau * 0.75  # Giảm 25% sau 3 giờ đầu

    # Tính tiền thuê sân
    if so_gio_thue <= 3:
        tien_san = so_gio_thue * don_gia_3h_dau
    else:
        tien_san = (3 * don_gia_3h_dau) + ((so_gio_thue - 3) * don_gia_sau_3h)

    # Kiểm tra nếu toàn bộ hoặc một phần thời gian thuê trong khoảng 11 - 15 giờ để giảm 10%
    if gio_bat_dau < 15 and gio_ket_thuc > 11:
        tien_san *= 0.9  # Giảm 10%

    # In kết quả
    print("Số tiền thuê sân phải trả là:", int(tien_san), "đồng")