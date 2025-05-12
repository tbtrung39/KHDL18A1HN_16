import Matranvuong

n = int(input("Nhập kích thước ma trận NxN (N >= 1): "))

mt = Matranvuong.nhap_ma_tran(n)

print("\n1. Ma trận ban đầu:")
Matranvuong.in_ma_tran(mt)

print("\n2. Ma trận chuyển vị:")
chuyenvi = Matranvuong.chuyen_vi(mt)
Matranvuong.in_ma_tran(chuyenvi)

print("\n3. Kiểm tra ma trận đối xứng:")
if Matranvuong.kiem_tra_doi_xung(mt):
    print("Ma trận đối xứng.")
else:
    print("Ma trận không đối xứng.")
