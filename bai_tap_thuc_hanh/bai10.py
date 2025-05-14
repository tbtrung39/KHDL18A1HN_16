#Cach1:
str1 = input("Nhap chuoi 1: ")
str2 = input("Nhap chuoi 2: ")
do_dai_max = 0
chuoi_con_dai_nhat =""
for i in range(len(str1)):
    for j in range(i + 1, len(str1) + 1):
        chuoi_con = str1[i:j]
        if chuoi_con in str2 and len(chuoi_con) > do_dai_max:
            do_dai_max = len(chuoi_con)
            chuoi_con_dai_nhat = chuoi_con
if chuoi_con_dai_nhat:
    print("Chuoi con chung dai nhat la:", chuoi_con_dai_nhat)
else:
    print("Khong co chuoi con chung.")

#Cach2:
max_len = 0  
max_doan_chung = ""  

for i in range(len(str1)):
    for j in range(i, len(str1)):
        doan_con = str1[i:j+1]  
        if doan_con in str2 and len(doan_con) > max_len:  
            max_len = len(doan_con)
            max_doan_chung = doan_con
print("Chuoi con chung dai nhat la:", max_doan_chung)