chuoi_str1 = input("Nhập chuỗi Str1: ")
chuoi_str2 = input("Nhập chuỗi Str2: ")
ket_qua = ""
i = 0
j = 0
while i < len(chuoi_str1) and j < len(chuoi_str2):
    ket_qua += chuoi_str1[i]
    ket_qua += chuoi_str2[j]
    i += 1
    j += 1
ket_qua += chuoi_str1[i:]
ket_qua += chuoi_str2[j:]
print("Chuỗi kết quả sau khi trộn:", ket_qua)