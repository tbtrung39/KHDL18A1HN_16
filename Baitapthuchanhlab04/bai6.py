so = int(input("Nhập số: "))
chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
chuoi_so = str(so)
ket_qua = ""

i = 0
while i < len(chuoi_so):
    ky_tu = chuoi_so[i]
    ket_qua += chu_so[int(ky_tu)] + " "
    i += 1

print(ket_qua)
