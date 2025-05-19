import quanlyhanghoa

def main():
    danh_sach_hang_hoa = []
    while True:
        print("\n--- Nhập thông tin mặt hàng ---")
        hang_hoa = quanlyhanghoa.nhap_thong_tin_mat_hang()
        danh_sach_hang_hoa.append(hang_hoa)

        tiep_tuc = input("Bạn có muốn nhập thêm mặt hàng khác không? (y/n): ").lower()
        if tiep_tuc != 'y':
            break

    quanlyhanghoa.hien_thi_danh_sach_hang_hoa(danh_sach_hang_hoa, "Danh sách hàng hóa trước khi sắp xếp")

    danh_sach_da_sap_xep = quanlyhanghoa.sap_xep_theo_thue_vat(danh_sach_hang_hoa)
    quanlyhanghoa.hien_thi_danh_sach_da_sap_xep(danh_sach_da_sap_xep, "Danh sách hàng hóa sau khi sắp xếp theo Thuế VAT (giảm dần)")

if __name__ == "__main__":
    main()