s1 = input("Chuỗi 1: ")
s2 = input("Chuỗi 2: ")
ket_qua = ""
i = 0
while i < len(s1) or i < len(s2):
    if i < len(s1):
        ket_qua = ket_qua + s1[i]
    if i < len(s2):
        ket_qua = ket_qua + s2[i]
    i = i + 1
print("Chuỗi trộn:", ket_qua)