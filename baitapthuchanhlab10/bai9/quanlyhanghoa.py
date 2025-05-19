class MatHang:
    def __init__(self, ma_hang, ten_hang, don_vi_tinh, don_gia, so_luong):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.don_vi_tinh = don_vi_tinh
        self.don_gia = don_gia
        self.so_luong = so_luong
        self.thanh_tien = self.don_gia * self.so_luong
        self.thue_vat = self.thanh_tien * 0.1

def nhap_thong_tin_mat_hang():
    while True:
        ma_hang = input("Nhập mã hàng (4 ký tự): ")
        if len(ma_hang) == 4:
            break
        else:
            print("Mã hàng phải là 4 ký tự. Vui lòng nhập lại.")

    ten_hang = input("Nhập tên hàng: ")
    don_vi_tinh = input("Nhập đơn vị tính: ")

    don_gia = float(input("Nhập đơn giá: "))
    so_luong = int(input("Nhập số lượng: "))

    return MatHang(ma_hang, ten_hang, don_vi_tinh, don_gia, so_luong)

def sap_xep_theo_thue_vat(danh_sach_hang_hoa, reverse=True):
    return sorted(danh_sach_hang_hoa, key=lambda hang: hang.thue_vat, reverse=reverse)

def hien_thi_danh_sach_hang_hoa(danh_sach_hang_hoa, title="Danh sách hàng hóa"):
    """Hiển thị danh sách thông tin hàng hóa."""
    print(f"\n--- {title} ---")
    for hang in danh_sach_hang_hoa:
        print(f"Mã hàng: {hang.ma_hang}, Tên hàng: {hang.ten_hang}, ĐVT: {hang.don_vi_tinh}, "
              f"Đơn giá: {hang.don_gia}, Số lượng: {hang.so_luong}, Thành tiền: {hang.thanh_tien:.2f}, "
              f"Thuế VAT: {hang.thue_vat:.2f}")

if __name__ == "__main__":
    print("Đây là module qlyhanghoa. Vui lòng chạy file chương trình chính để sử dụng.")