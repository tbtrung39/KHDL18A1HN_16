def nhap_danh_sach_hang_hoa():
    danh_sach = []
    n = int(input("Nhập số lượng mặt hàng: "))
    for i in range(n):
        print(f"\nNhập thông tin mặt hàng thứ {i + 1}:")
        ma_hang = input("  Mã hàng (4 ký tự): ").strip()
        ten_hang = input("  Tên hàng: ").strip()
        don_vi = input("  Đơn vị tính: ").strip()
        don_gia = float(input("  Đơn giá: "))
        so_luong = int(input("  Số lượng: "))
        
        mat_hang = {
            "ma_hang": ma_hang,
            "ten_hang": ten_hang,
            "don_vi": don_vi,
            "don_gia": don_gia,
            "so_luong": so_luong,
            "thanh_tien": 0,
            "thue": 0
        }
        danh_sach.append(mat_hang)
    return danh_sach

def tinh_thanh_tien_va_thue(ds):
    for item in ds:
        item["thanh_tien"] = item["don_gia"] * item["so_luong"]
        item["thue"] = item["thanh_tien"] * 0.10

def in_danh_sach(ds, title="Danh sách mặt hàng"):
    print(f"\n{title}")
    print("-" * 90)
    print(f"{'Mã':<6} {'Tên hàng':<20} {'ĐVT':<10} {'Đơn giá':<10} {'SL':<5} {'Thành tiền':<15} {'Thuế':<10}")
    print("-" * 90)
    for item in ds:
        print(f"{item['ma_hang']:<6} {item['ten_hang']:<20} {item['don_vi']:<10} "
              f"{item['don_gia']:<10.2f} {item['so_luong']:<5} {item['thanh_tien']:<15.2f} {item['thue']:<10.2f}")
    print("-" * 90)

def sap_xep_theo_thue_giam_dan(ds):
    ds.sort(key=lambda x: x["thue"], reverse=True)