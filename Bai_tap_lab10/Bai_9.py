class MatHang:
    def __init__(self, ma_hang, ten_hang, don_vi_tinh, don_gia, so_luong):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.don_vi_tinh = don_vi_tinh
        self.don_gia = don_gia
        self.so_luong = so_luong
        self.thanh_tien = self.tinh_thanh_tien()
        self.thue_vat = self.tinh_thue_vat()
    def tinh_thanh_tien(self):
        return self.don_gia * self.so_luong
    
    def tinh_thue_vat(self):
        return self.thanh_tien * 0.1
    
    def __str__(self):
        return f"{self.ma_hang} | {self.ten_hang:20} | {self.don_vi_tinh:10} | {self.don_gia:10.2f} | {self.so_luong:5} | {self.thanh_tien:12.2f} | {self.thue_vat:10.2f}"
def nhap_mat_hang():
    """Nhập thông tin mặt hàng từ bàn phím"""
    ma_hang = input("Nhập mã hàng (4 ký tự): ")
    ten_hang = input("Nhập tên hàng: ")
    don_vi_tinh = input("Nhập đơn vị tính: ")
    don_gia = float(input("Nhập đơn giá: "))
    so_luong = int(input("Nhập số lượng: "))
    return MatHang(ma_hang, ten_hang, don_vi_tinh, don_gia, so_luong)
def sap_xep_theo_thue(danh_sach):
    """Sắp xếp giảm dần theo thuế VAT"""
    return sorted(danh_sach, key=lambda x: x.thue_vat, reverse=True)
def in_danh_sach(danh_sach, tieu_de):
    """In danh sách mặt hàng"""
    print("\n" + "="*100)
    print(tieu_de.center(100))
    print("="*100)
    print("Mã hàng | Tên hàng              | Đơn vị tính | Đơn giá   | Số lượng | Thành tiền   | Thuế VAT")
    print("-"*100)
    for item in danh_sach:
        print(item)
    print("="*100)
def main():
    danh_sach = []
    while True:
        print("\n1. Thêm mặt hàng")
        print("2. Hiển thị và sắp xếp")
        print("3. Thoát")
        chon = input("Chọn chức năng: ")
        
        if chon == '1':
            danh_sach.append(nhap_mat_hang())
        elif chon == '2':
            if not danh_sach:
                print("Danh sách trống!")
                continue
            in_danh_sach(danh_sach, "DANH SÁCH TRƯỚC KHI SẮP XẾP")
            danh_sach_sx = sap_xep_theo_thue(danh_sach)
            in_danh_sach(danh_sach_sx, "DANH SÁCH SAU KHI SẮP XẾP GIẢM DẦN THEO THUẾ")
        elif chon == '3':
            break
if __name__ == "__main__":
    main()