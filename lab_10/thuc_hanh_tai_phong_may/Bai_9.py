import qlyhanghoa

def main():
    print("=== QUẢN LÝ HÀNG HÓA SIÊU THỊ ===")
    ds_hang = qlyhanghoa.nhap_hang_hoa()

    print("\n DANH SÁCH HÀNG HÓA (Trước khi sắp xếp):")
    qlyhanghoa.in_danh_sach(ds_hang)

    ds_sap_xep = qlyhanghoa.sap_xep_theo_thue(ds_hang)

    print("\n DANH SÁCH HÀNG HÓA (Đã sắp xếp theo Thuế giảm dần):")
    qlyhanghoa.in_danh_sach(ds_sap_xep)

if __name__ == "__main__":
    main()