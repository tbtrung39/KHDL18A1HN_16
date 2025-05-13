import matranvuong

N = int(input("Nhập kích thước ma trận vuông N: "))

matran = matranvuong.nhap_ma_tran(N)
matranvuong.in_ma_tran(matran)

matran_cv = matranvuong.chuyen_vi(matran)
print("\nMa trận chuyển vị:")
matranvuong.in_ma_tran(matran_cv)

if matranvuong.kiem_tra_doi_xung(matran):
    print("\nMa trận là ma trận đối xứng.")
else:
    print("\nMa trận không phải là ma trận đối xứng.")