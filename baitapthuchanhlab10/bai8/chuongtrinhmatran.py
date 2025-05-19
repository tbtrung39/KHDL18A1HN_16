import matranvuong

def main():
    print("--- Chương trình xử lý ma trận vuông ---")
    n = matranvuong.nhap_kich_thuoc()
    ma_tran = matranvuong.nhap_ma_tran(n)

    print("\nMa trận đã nhập:")
    matranvuong.in_ma_tran(ma_tran)

    ma_tran_chuyen_vi = matranvuong.chuyen_vi_ma_tran(ma_tran)
    print("\nMa trận chuyển vị:")
    matranvuong.in_ma_tran(ma_tran_chuyen_vi)

    if matranvuong.la_ma_tran_doi_xung(ma_tran):
        print("\nMa trận là ma trận đối xứng.")
    else:
        print("\nMa trận không phải là ma trận đối xứng.")

if __name__ == "__main__":
    main()