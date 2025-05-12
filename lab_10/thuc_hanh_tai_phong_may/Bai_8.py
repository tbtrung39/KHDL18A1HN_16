# bai_8.py

import Matranvuong

def main():
    n = int(input("Nhập kích thước N của ma trận vuông NxN: "))
    m = Matranvuong.nhap_ma_tran(n)

    print("\nMa trận vừa nhập:")
    Matranvuong.in_ma_tran(m)

    print("\nMa trận chuyển vị:")
    mt_cv = Matranvuong.chuyen_vi(m)
    Matranvuong.in_ma_tran(mt_cv)

    if Matranvuong.kiem_tra_doi_xung(m):
        print("\nMa trận là ma trận đối xứng.")
    else:
        print("\nMa trận không phải là ma trận đối xứng.")

if __name__ == "__main__":
    main()