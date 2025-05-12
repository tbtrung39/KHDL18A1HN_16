import Matranvuong

n = int(input("Nhap kich thuoc ma tran vuong N: "))
m = Matranvuong.nhap_ma_tran(n)

Matranvuong.in_ma_tran(m)

print("\nMa tran chuyen vi:")
mt_chuyen_vi = Matranvuong.chuyen_vi(m)
Matranvuong.in_ma_tran(mt_chuyen_vi)

if Matranvuong.kiem_tra_doi_xung(m):
    print("La Ma tran doi xung")
else:
    print("Khong phai ma tran doi xung")
