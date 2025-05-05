#Bước 1(Bài 9):
def nhap_hang_hoa():
    ma_hang = input("Nhập mã hàng (4 ký tự): ")
    ten_hang = input("Nhập tên hàng: ")
    don_vi_tinh = input("Nhập đơn vị tính: ")
    don_gia = float(input("Nhập đơn giá: "))
    so_luong = int(input("Nhập số lượng: "))
    return {
        'ma_hang': ma_hang,
        'ten_hang': ten_hang,
        'don_vi_tinh': don_vi_tinh,
        'don_gia': don_gia,
        'so_luong': so_luong
    }

def tinh_thanh_tien(hang_hoa):
    hang_hoa['thanh_tien'] = hang_hoa['don_gia'] * hang_hoa['so_luong']
    return hang_hoa

def tinh_thue(hang_hoa):
    hang_hoa['thue'] = hang_hoa['thanh_tien'] * 0.1
    return hang_hoa

def sap_xep_hang_hoa(danh_sach_hang_hoa):
    return sorted(danh_sach_hang_hoa, key=lambda x: x['thue'], reverse=True)