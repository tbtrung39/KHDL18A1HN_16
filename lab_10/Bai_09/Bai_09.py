#Bước 2(Bài 9):
import qlyhanghoa

def main():
    """Chương trình chính."""
    danh_sach_hang_hoa = []
    n = int(input("Nhập số lượng mặt hàng: "))

    for _ in range(n):
        hang_hoa = qlyhanghoa.nhap_hang_hoa()
        hang_hoa = qlyhanghoa.tinh_thanh_tien(hang_hoa)
        hang_hoa = qlyhanghoa.tinh_thue(hang_hoa)
        danh_sach_hang_hoa.append(hang_hoa)

    print("\nDanh sách hàng hóa trước khi sắp xếp:")
    for hang_hoa in danh_sach_hang_hoa:
        print(hang_hoa)

    danh_sach_hang_hoa_da_sap_xep = qlyhanghoa.sap_xep_hang_hoa(danh_sach_hang_hoa)

    print("\nDanh sách hàng hóa sau khi sắp xếp theo thuế (giảm dần):")
    for hang_hoa in danh_sach_hang_hoa_da_sap_xep:
        print(hang_hoa)

if __name__ == "__main__":
    main()

    #Bước 2(Bài 8):
import matranvuong

ma_tran = matranvuong.nhap_ma_tran()
print("Ma trận vừa nhập:")
matranvuong.in_ma_tran(ma_tran)
ma_tran_chuyen_vi = matranvuong.tinh_ma_tran_chuyen_vi(ma_tran)
print("Ma trận chuyển vị:")
matranvuong.in_ma_tran(ma_tran_chuyen_vi)
doi_xung = matranvuong.kiem_tra_doi_xung(ma_tran)
print("Ma trận có đối xứng không:", doi_xung)