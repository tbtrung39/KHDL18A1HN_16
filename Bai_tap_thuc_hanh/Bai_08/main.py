import Matranvuong as mt

n = int(input("Nhập kích thước ma trận: "))
mat = mt.nhap_ma_tran(n)
print("Ma trận:")
mt.in_ma_tran(mat)
print("Chuyển vị:")
mt.in_ma_tran(mt.chuyen_vi(mat))
print("Có đối xứng không?", mt.kiem_tra_doi_xung(mat))
