so = int(input("Nhập một số thập phân: "))

chu_so = {
    0: "không", 1: "một", 2: "hai", 3: "ba", 4: "bốn",
    5: "năm", 6: "sáu", 7: "bảy", 8: "tám", 9: "chín"
}

so_chuoi = str(so)
ket_qua = ""
i = 0
while i < len(so_chuoi):
    chu_so_hien_tai = int(so_chuoi[i])
    ket_qua += chu_so[chu_so_hien_tai] + " "
    i += 1

if ket_qua and ket_qua[-1] == " ":
    ket_qua = ket_qua[:-1]

print(ket_qua)