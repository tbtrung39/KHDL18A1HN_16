chuoi_str = input("Nhập chuỗi Str: ")
do_dai_max = 0
ket_qua = ""
i = 0
while i < len(chuoi_str):
    j = i
    while j < len(chuoi_str) and chuoi_str[i] == chuoi_str[j]:
        j += 1
    if j - i > do_dai_max:
        do_dai_max = j - i
        ket_qua = chuoi_str[i:j]
    i = j
print("Chuỗi con dài nhất có các phần tử giống nhau:", ket_qua)