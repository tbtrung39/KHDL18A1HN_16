chu_so_chu = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
so = input("Nhập một số thập phân: ")
vi_tri_cham = -1
i = 0
while i < len(so):
    if so[i] == ".":
        vi_tri_cham = i
        break
    i += 1
if vi_tri_cham == -1:
    phan_nguyen = so
    phan_thap_phan = ""
else:
    phan_nguyen = so[:vi_tri_cham]  
    phan_thap_phan = so[vi_tri_cham+1:]  
ket_qua = ""
i = 0
while i < len(phan_nguyen):
    chu_so = int(phan_nguyen[i])
    ket_qua += chu_so_chu[chu_so] + " "
    i += 1
if phan_thap_phan:
    ket_qua += "phẩy "
i = 0
while i < len(phan_thap_phan):
    chu_so = int(phan_thap_phan[i])
    ket_qua += chu_so_chu[chu_so] + " "
    i += 1
print("Dạng chữ:", ket_qua)
