def nhap_ds_hang():
    ds = []
    n = int(input("Nhap so mat hang: "))
    for i in range(n):
        print(f"\nNhap thong tin mat hang thu {i+1}:")
        ma_hang = input("Ma hang (4 ky tu): ")
        ten_hang = input("Ten hang: ")
        don_vi = input("Don vi tinh: ")
        don_gia = float(input("Don gia: "))
        so_luong = int(input("So luong: "))

        mat_hang = {
            "ma_hang": ma_hang,
            "ten_hang": ten_hang,
            "don_vi": don_vi,
            "don_gia": don_gia,
            "so_luong": so_luong,
            "thanh_tien": 0,
            "thue": 0
        }

        ds.append(mat_hang)
    return ds

def tinh_thanh_tien_va_thue(ds):
    for mh in ds:
        mh["thanh_tien"] = mh["don_gia"] * mh["so_luong"]
        mh["thue"] = mh["thanh_tien"] * 0.1

def in_danh_sach(ds, tieu_de="Danh sach mat hang"):
    print("\n" + tieu_de)
    print("-" * 80)
    print(f"{'Ma':<6} {'Ten hang':<20} {'Don vi':<10} {'Don gia':<10} {'So luong':<10} {'Thanh tien':<15} {'Thue':<10}")
    print("-" * 80)
    for mh in ds:
        print(f"{mh['ma_hang']:<6} {mh['ten_hang']:<20} {mh['don_vi']:<10} {mh['don_gia']:<10.2f} {mh['so_luong']:<10} {mh['thanh_tien']:<15.2f} {mh['thue']:<10.2f}")
    print("-" * 80)

def sap_xep_theo_thue_giam(ds):
    return sorted(ds, key=lambda mh: mh["thue"], reverse=True)
