str1 = input("Nhập chuỗi Str1: ")
str2 = input("Nhập chuỗi Str2: ")
chuoi_con_chung_dai_nhat = ""
do_dai_lon_nhat  = 0
for i in range(len(str1)):
    for j in range(len(str2)):
        k = 0
        while i + k < len(str1) and j + k < len(str2) and str1[i + k] == str2[j + k]:
            k += 1
        if k > do_dai_lon_nhat :
            do_dai_lon_nhat  = k
            chuoi_con_chung_dai_nhat = str1[i:i + k]
print("Chuỗi con chung dài nhất:", chuoi_con_chung_dai_nhat)