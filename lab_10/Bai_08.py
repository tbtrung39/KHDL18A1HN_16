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