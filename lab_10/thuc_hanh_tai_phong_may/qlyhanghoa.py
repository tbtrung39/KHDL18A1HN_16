def nhap_hang_hoa():
    n = int(input("Nhập số lượng mặt hàng: "))
    ds_hang = []
    for i in range(n):
        print(f"\n--- Mặt hàng thứ {i + 1} ---")
        ma = input("Mã hàng (4 ký tự): ")
        while len(ma) != 4:
            print("Mã hàng phải đúng 4 ký tự.")
            ma = input("Nhập lại mã hàng: ")

        ten = input("Tên hàng: ")
        don_vi = input("Đơn vị tính: ")
        don_gia = float(input("Đơn giá: "))
        so_luong = int(input("Số lượng: "))

        thanh_tien = don_gia * so_luong
        thue = thanh_tien * 0.1

        hang = {
            'ma': ma,
            'ten': ten,
            'don_vi': don_vi,
            'don_gia': don_gia,
            'so_luong': so_luong,
            'thanh_tien': thanh_tien,
            'thue': thue
        }
        ds_hang.append(hang)
    return ds_hang

def in_danh_sach(ds):
    print("\n{:<6} {:<15} {:<10} {:<10} {:<10} {:<15} {:<10}".format(
        "Mã", "Tên hàng", "Đơn vị", "Đơn giá", "Số lượng", "Thành tiền", "Thuế"))
    print("-" * 80)
    for hang in ds:
        print("{:<6} {:<15} {:<10} {:<10.2f} {:<10} {:<15.2f} {:<10.2f}".format(
            hang['ma'], hang['ten'], hang['don_vi'], hang['don_gia'],
            hang['so_luong'], hang['thanh_tien'], hang['thue']
        ))

def sap_xep_theo_thue(ds):
    return sorted(ds, key=lambda x: x['thue'], reverse=True)