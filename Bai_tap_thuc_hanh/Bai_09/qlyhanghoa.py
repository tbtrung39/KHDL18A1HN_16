
def nhap_danh_sach():
    ds = []
    n = int(input("Nhập số lượng mặt hàng: "))
    for i in range(n):
        print(f"\nNhập thông tin mặt hàng thứ {i+1}:")
        ma = input("  Mã hàng (4 ký tự): ")
        ten = input("  Tên hàng: ")
        don_vi = input("  Đơn vị tính: ")
        don_gia = float(input("  Đơn giá: "))
        so_luong = int(input("  Số lượng: "))
        thanh_tien = don_gia * so_luong
        thue = thanh_tien * 0.10
        mh = {
            "ma": ma,
            "ten": ten,
            "don_vi": don_vi,
            "don_gia": don_gia,
            "so_luong": so_luong,
            "thanh_tien": thanh_tien,
            "thue": thue
        }
        ds.append(mh)
    return ds

def in_danh_sach(ds):
    print(f"\n{'Mã':<6} {'Tên hàng':<15} {'Đơn vị':<10} {'Đơn giá':<10} {'S.lượng':<8} {'Thành tiền':<12} {'Thuế':<10}")
    print("-" * 75)
    for mh in ds:
        print(f"{mh['ma']:<6} {mh['ten']:<15} {mh['don_vi']:<10} {mh['don_gia']:<10,.0f} {mh['so_luong']:<8} {mh['thanh_tien']:<12,.0f} {mh['thue']:<10,.0f}")

def sap_xep_theo_thue(ds):
    return sorted(ds, key=lambda mh: mh["thue"], reverse=True)
